from python_helper import log
from python_framework import Service, ServiceMethod, EnumItem


@Service()
class VoiceService :

    @ServiceMethod(requestClass=[[str]])
    def speakAll(self, textList) :
        serviceReturn = None
        try:
            serviceReturn = self.client.voice.speakAll(textList)
        except Exception as exception:
            log.warning(self.speakAll, 'Not possible to speak all', exception=exception, muteStackTrace=True)
        return serviceReturn
