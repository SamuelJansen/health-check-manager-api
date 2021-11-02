from python_helper import Constant as c
from python_helper import log, StringHelper
from python_framework import Service, ServiceMethod, EnumItem


@Service()
class HealthCheckService :

    @ServiceMethod()
    def checkAll(self) :
        reponseDictionary = {}
        for api in self.service.api.findAll():
            response = {}
            try:
                response = self.client.healthCheck.checkHealth(f'{api.healthUrl}')
            except Exception as exception:
                response = {'status':'DOWN', 'message': exception.message, 'logMessage': exception.logMessage}
                exceptionMessage = f'{exception.message if exception.status < 500 else exception.logMessage}'
                if 120 < len(exceptionMessage):
                    exceptionMessage = str(StringHelper.join(exceptionMessage.split(c.COLON)[-2:], character=c.BLANK))[-120:]
                message = f'{api.name} {api.environment.lower()} api is down{c.DOT_SPACE_CAUSE}{exceptionMessage}'
                self.service.voice.speakAll([message])
            reponseDictionary[f'{api.environment}{c.COLON}{api.key}{c.COLON}{api.name}'] = response
        log.prettyPython(self.checkAll, 'Apis status', reponseDictionary, logLevel=log.STATUS)
        return reponseDictionary
