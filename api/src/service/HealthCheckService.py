from python_helper import Constant as c
from python_helper import log, StringHelper
from python_framework import Service, ServiceMethod, GlobalException, HttpStatus, EnumItem


@Service()
class HealthCheckService :

    @ServiceMethod()
    def checkAll(self) :
        reponseDictionary = {}
        for environment in self.service.environment.findAll():
            response = {}
            responseStatus = HttpStatus.INTERNAL_SERVER_ERROR
            formatedAdditionalMessage = f'{c.BLANK}'
            try:
                response, responseHeader, responseStatus = self.client.healthCheck.checkHealth(f'{environment.healthUrl}')
            except GlobalException as globalException:
                log.log(self.checkAll, 'Not possible to check environment', exception=globalException, muteStackTrace=True)
                response = {
                    'status':'DOWN',
                    'message': globalException.message,
                    'logMessage': globalException.logMessage
                }
                responseHeader = {}
                responseStatus = globalException.status
                self.notificateError(environment, globalException)
            reponseDictionary[self.helper.healthCheck.getEnvironmentResponseKey(environment)] = {
                'response': response,
                'status': responseStatus
            }
        log.prettyPython(self.checkAll, 'Apis status', reponseDictionary, logLevel=log.STATUS)
        return reponseDictionary


    @ServiceMethod(requestClass=[EnumItem, GlobalException])
    def notificateError(self, environment, globalException):
        self.service.voice.speak(self.helper.healthCheck.getFormattedErrorMessage(environment, globalException))
