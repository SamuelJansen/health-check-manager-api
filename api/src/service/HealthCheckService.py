import requests

from python_helper import Constant as c
from python_helper import log, StringHelper, ObjectHelper
from python_framework import Service, ServiceMethod, GlobalException, HttpStatus, EnumItem, HttpDomain, FlaskUtil


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
                clientResponse = globalException.logPayload.get(HttpDomain.RESPONSE_BODY_KEY, {}).get(FlaskUtil.CLIENT_RESPONSE)
                log.failure(self.checkAll, 'Not possible to check environment', exception=globalException, muteStackTrace=True)
                response = {
                    'status':'DOWN',
                    'message': globalException.message,
                    'logMessage': globalException.logMessage,
                    'debug': c.BLANK if ObjectHelper.isNone(clientResponse) else clientResponse.text
                }
                self.notifyError(environment, globalException, clientResponse)
            reponseDictionary[self.helper.healthCheck.getEnvironmentResponseKey(environment)] = {
                'response': response,
                'status': responseStatus
            }
        log.prettyPython(self.checkAll, 'Apis status', reponseDictionary, logLevel=log.STATUS)
        return reponseDictionary


    @ServiceMethod(requestClass=[EnumItem, GlobalException, requests.Response])
    def notifyError(self, environment, globalException, clientResponse):
        self.service.notification.notifyError(self.helper.healthCheck.getFormattedErrorMessage(environment, globalException, clientResponse))
