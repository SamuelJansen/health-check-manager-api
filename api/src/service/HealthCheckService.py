from python_helper import log
from python_framework import Service, ServiceMethod, EnumItem

# from enumeration.HealthCheckApiList import HealthCheckApiList

@Service()
class HealthCheckService :

    @ServiceMethod()
    def checkAll(self) :
        # reponseDictionary = {}
        # for enum in [
        #     HealthCheckApiList.SPEECH_API,
        #     HealthCheckApiList.RIACHUELO_AUTOMATING_API,
        #     HealthCheckApiList.NGROK_MANAGER_API,
        #     HealthCheckApiList.IDEALIZAR_AGENDA_API,
        #     HealthCheckApiList.IDEALIZAR_WHATS_APP_WEB_API,
        #     HealthCheckApiList.IDEALIZAR_WHATS_APP_MANAGER_API
        # ] :
        #     reponseDictionary[enum.enumName] = self.client.healthCheck.check(enum.url)
        # log.prettyPython(self.checkAll, 'reponseDictionary', reponseDictionary, logLevel=log.DEBUG)
        return reponseDictionary
