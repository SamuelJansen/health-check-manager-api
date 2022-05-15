from python_helper import log
from python_framework import Service, ServiceMethod, EnumItem


@Service()
class VoiceService:

    @ServiceMethod(requestClass=[str])
    def speak(self, text) :
        serviceReturn = None
        try:
            serviceReturn = self.emitter.voice.speakAll([{"text": text}])
        except Exception as exception:
            log.failure(self.speakAll, 'Not possible to speak all', exception=exception, muteStackTrace=True)
        return serviceReturn
