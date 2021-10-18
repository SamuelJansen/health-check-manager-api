from python_framework import Service, ServiceMethod, EnumItem


@Service()
class VoiceService :

    @ServiceMethod(requestClass=[[str]])
    def speakAll(self, textList) :
        return self.client.voice.speakAll(textList)
