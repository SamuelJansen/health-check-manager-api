from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from python_framework import Service, ServiceMethod, EnumItem


@Service()
class VoiceService:

    @ServiceMethod(requestClass=[[str]])
    def speakAll(self, textList) :
        serviceReturn = None
        try:
            serviceReturn = self.emitter.voice.speakAll([{"text": text} for text in textList])
        except Exception as exception:
            log.failure(self.speakAll, 'Not possible to speak all', exception=exception, muteStackTrace=True)
        return serviceReturn


    @ServiceMethod(requestClass=[str])
    def speak(self, text) :
        serviceReturn = None
        try:
            serviceReturn = self.speakAll([text])
        except Exception as exception:
            log.failure(self.speak, 'Not possible to speak', exception=exception, muteStackTrace=True)
        return serviceReturn
