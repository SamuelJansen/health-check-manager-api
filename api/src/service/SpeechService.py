from python_framework import Service, ServiceMethod, EnumItem

from dto import SpeakDto

@Service()
class SpeechService :

    @ServiceMethod(requestClass=[[SpeakDto.SpeakRequestDto]])
    def speakAll(self, textList) :
        return self.client.speech.speakAll([SpeakDto.SpeakRequestDto(text=text) for text in textList])
