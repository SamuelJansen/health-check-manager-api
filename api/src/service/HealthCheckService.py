from python_helper import Constant as c
from python_helper import log, StringHelper
from python_framework import Service, ServiceMethod, EnumItem, GlobalException, HttpStatus


@Service()
class HealthCheckService :

    @ServiceMethod()
    def checkAll(self) :
        errorMessages = []
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
                responseStatus = globalException.status
                exceptionMessage = f'{globalException.message if responseStatus < 500 else globalException.logMessage}'
                if 120 < len(exceptionMessage):
                    exceptionMessage = str(StringHelper.join(exceptionMessage.split(c.COLON)[-2:], character=c.BLANK))[-120:]
                formatedAdditionalMessage = f'{c.DOT_SPACE_CAUSE}{exceptionMessage}'
            if HttpStatus.BAD_REQUEST <= responseStatus:
                errorMessages.append(f'{environment.apiName} {environment.name.lower()} environment is down{formatedAdditionalMessage}')
            reponseDictionary[f'{environment.name}{c.COLON}{environment.apiKey}{c.COLON}{environment.apiName}'] = {
                'response': response,
                'status': responseStatus
            }
        self.service.voice.speakAll(errorMessages)
        log.prettyPython(self.checkAll, 'Apis status', reponseDictionary, logLevel=log.STATUS)
        return reponseDictionary
