from python_helper import Constant as c
from python_helper import log, StringHelper
from python_framework import Service, ServiceMethod, EnumItem

# from enumeration.HealthCheckApiList import HealthCheckApiList

@Service()
class HealthCheckService :

    @ServiceMethod()
    def checkAll(self) :
        reponseDictionary = {}
        for api in self.service.api.findAll():
            response = {}
            try:
                response = self.client.healthCheck.checkHealth(api.host)
            except Exception as exception:
                response = {'status':'DOWN', 'message': exception.message, 'logMessage': exception.logMessage}
                exceptionMessage = f'{exception.message if exception.status < 500 else exception.logMessage}'
                if 120 < len(exceptionMessage):
                    exceptionMessage = str(StringHelper.join(exceptionMessage.split(c.COLON)[-2:], character=c.BLANK))[-120:]
                    print(exceptionMessage)
                message = f'{api.name} {api.environment.enumName.lower()} api is down{c.DOT_SPACE_CAUSE}{exceptionMessage}'
                # print(message)
                # message = f'{api.name} {api.environment.enumName.lower()} api is down{c.DOT_SPACE_CAUSE}{exception.message}'
                self.service.voice.speakAll([message])
            reponseDictionary[f'{api.key}{c.COLON}{api.name}{c.COLON}{api.type}'] = response
        log.prettyPython(self.checkAll, 'Apis status', reponseDictionary, logLevel=log.INFO)
        return reponseDictionary
