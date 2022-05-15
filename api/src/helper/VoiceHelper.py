from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from python_framework import Helper, HelperMethod, EnumItem


@Helper()
class VoiceHelper:

    @HelperMethod(requestClass=[EnumItem])
    def getEnumAsSpeech(self, enum) :
        return self.getConstantNameAsSpeech(enum.enumName)


    @HelperMethod(requestClass=[str])
    def getConstantNameAsSpeech(self, enumName) :
        serviceReturn = None
        try:
            serviceReturn = StringHelper.join(self.getConstantNameAsSpeechList(enumName), character=c.SPACE)
        except Exception as exception:
             log.warning(self.getConstantNameAsSpeech, 'Not possible to parse name as speech', exception=exception, muteStackTrace=True)
        return serviceReturn


    @HelperMethod(requestClass=[str])
    def getConstantNameAsSpeechList(self, enumName) :
        serviceReturn = None
        try:
            serviceReturn = [] if ObjectHelper.isNone(enumName) else enumName.lower().split(c.UNDERSCORE)
        except Exception as exception:
             log.warning(self.getConstantNameAsSpeechList, 'Not possible to parse constant as speech list', exception=exception, muteStackTrace=True)
        return serviceReturn
