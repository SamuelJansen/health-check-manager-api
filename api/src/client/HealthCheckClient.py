import requests
from python_helper import log, ObjectHelper
from python_framework import Client, ClientMethod, HttpStatus

from config import HealthCheckConfig

ACTUATOR_HEALTH_URI = '/actuator/health'

@Client()
class HealthCheckClient :

    @ClientMethod(requestClass=[str])
    def check(self, url) :
        response = None
        print(url)
        try :
            response = requests.get(f'{url}{ACTUATOR_HEALTH_URI}', timeout=HealthCheckConfig.CLIENT_CHECK_REQUEST_TIME_OUT_IN_SECONDS)
        except Exception as exception :
            log.failure(self.check, f'Not possible to check {url}', exception=exception, muteStackTrace=True)
        responseAsJson = {}
        try :
            responseAsJson = response.json()
        except Exception as exception :
            log.warning(self.check, 'Not possible to parse response as json', exception=exception, muteStackTrace=True)
        return responseAsJson, HttpStatus.map(500 if ObjectHelper.isNone(response) else response.status_code)
