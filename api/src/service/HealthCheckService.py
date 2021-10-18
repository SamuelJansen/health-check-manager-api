from python_helper import Constant as c
from python_helper import log
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
            reponseDictionary[f'{api.key}{c.COLON}{api.name}{c.COLON}{api.type}'] = response
        log.prettyPython(self.checkAll, 'Apis status', reponseDictionary, logLevel=log.INFO)
        return reponseDictionary
