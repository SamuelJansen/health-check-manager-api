import requests
from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from python_framework import HttpClient, HttpClientMethod, HttpStatus, GlobalException

from config import VoiceClientConfig


@HttpClient(
    url = VoiceClientConfig.BASE_URL,
    headers = {
        'Api-Key': f'Bearer {VoiceClientConfig.API_KEY}'
    },
    timeout = VoiceClientConfig.DEFAULT_TIMEOUT_IN_SECONDS,
)
class VoiceClient :

    @HttpClientMethod(
        url = '/speech',
        requestClass=[[str]]
    )
    def speakAll(self, textList):
        return self.post(body=[{"text": text} for text in textList])
