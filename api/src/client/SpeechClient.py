import requests
from python_helper import log
from python_framework import Client, ClientMethod, HttpStatus

from config import SpeechClientConfig
from dto import SpeakDto

SPEECH_URL = f'{SpeechClientConfig.BASE_URL}/speech'

@Client()
class SpeechClient :

    @ClientMethod(requestClass=[[SpeakDto.SpeakRequestDto]])
    def speakAll(self, speakRequestDtoList):
        requestDtoList = [
            {
                "text": speakRequestDto.text
            } for speakRequestDto in speakRequestDtoList
        ]
        response = None
        try :
            response = requests.post(SPEECH_URL, json=requestDtoList)
        except Exception as exception :
            log.failure(self.speakAll, 'Not possible to speak', exception=exception, muteStackTrace=True)
        responseAsJson = {}
        try :
            responseAsJson = response.json()
        except Exception as exception :
            log.warning(self.speakAll, 'Not possible to parse response as json', exception=exception, muteStackTrace=True)
        return responseAsJson, HttpStatus.map(response.status_code)
