from python_helper import log
from python_framework import Service, ServiceMethod, EnumItem


@Service()
class VoiceService :

    @ServiceMethod(requestClass=[[str]])
    def speakAll(self, textList) :
        response = None
        try:
            response = elf.client.voice.speakAll(textList)
        except Exception as exception:
            log.failure(self.speakAll, 'Not possible to speack all', exception=exception, muteStackTrace=True)
        return response
