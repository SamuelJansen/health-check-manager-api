import requests
from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from python_framework import Client, ClientMethod, HttpStatus, GlobalException

from config import HealthCheckConfig


BASIC_HEADERS = basicHeaders = {
    'Content-type': 'application/json'
}

CLIENT_DID_NOT_SENT_ANY_MESSAGE = 'Client did not sent any message'
ERROR_AT_CLIENT_CALL_MESSAGE = 'Error at client call'


@Client()
class HealthCheckClient :

    @ClientMethod(requestClass=[str])
    def checkHealth(self, url) :
        response = None
        try :
            response = requests.get(url, headers=BASIC_HEADERS, timeout=HealthCheckConfig.CLIENT_CHECK_REQUEST_TIME_OUT_IN_SECONDS)
        except Exception as exception:
            self.raiseException(response, exception)
        self.raiseExceptionIfNeeded(response)
        return self.getCompleteResponseAsJson(response)

    def raiseException(self, response, exception):
        raise GlobalException(
            logMessage = self.getErrorMessage(response, exception=exception)
        )

    def raiseExceptionIfNeeded(self, response):
        if ObjectHelper.isNone(response) or ObjectHelper.isNone(response.status_code) or 500 <= response.status_code:
            raise GlobalException(logMessage = self.getErrorMessage(response))
        elif 400 <= response.status_code :
            raise GlobalException(
                message = self.getErrorMessage(response),
                status = HttpStatus.map(response.status_code),
                logMessage = ERROR_AT_CLIENT_CALL_MESSAGE
            )

    def getCompleteResponseAsJson(self, response, fallbackStatus=HttpStatus.INTERNAL_SERVER_ERROR):
        responseBody, responseStatus = None, None
        try :
            responseBody, responseStatus = response.json(), HttpStatus.map(HttpStatus.NOT_FOUND if ObjectHelper.isNone(response.status_code) else response.status_code)
        except Exception as exception :
            tempStatus = None
            responseBody, responseStatus = None, HttpStatus.map(fallbackStatus)
            log.failure(self.getCompleteResponseAsJson, 'Not possible to parse response as json', exception=exception, muteStackTrace=True)
        return responseBody, responseStatus

    def getErrorMessage(self, response, exception=None):
        errorMessage = CLIENT_DID_NOT_SENT_ANY_MESSAGE
        possibleErrorMessage = None
        try :
            if ObjectHelper.isNotNone(response):
                possibleErrorMessage = response.json().get('message', response.json().get('error')).strip()
            if ObjectHelper.isNotNone(possibleErrorMessage) and StringHelper.isNotBlank(possibleErrorMessage):
                errorMessage = f'{c.DOT_SPACE_CAUSE}{possibleErrorMessage}'
            else:
                log.prettyPython(self.getErrorMessage, 'Client response', response.json(), logLevel=log.DEBUG)
        except Exception as innerException :
            log.warning(self.getErrorMessage, 'Not possible to get error message from response', exception=innerException)
        exceptionPortion = ERROR_AT_CLIENT_CALL_MESSAGE if ObjectHelper.isNone(exception) or StringHelper.isBlank(exception) else str(exception)
        return f'{exceptionPortion}{c.DOT_SPACE}{errorMessage}'
