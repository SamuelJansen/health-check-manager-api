import requests

from python_helper import Constant as c
from python_helper import log, StringHelper, ObjectHelper
from python_framework import Helper, HelperMethod, EnumItem, GlobalException, HttpStatus, EnumItem

from constant import HealthCheckConstant


@Helper()
class HealthCheckHelper:

        @HelperMethod(requestClass=[EnumItem, GlobalException, requests.Response])
        def getFormattedErrorMessage(self, environment, globalException, clientResponse):
            formatedAdditionalMessage = self.getFormattedAdditionalMessage(globalException, clientResponse)
            return f'{environment.apiName} {environment.name.lower()} environment is down{formatedAdditionalMessage}'


        @HelperMethod(requestClass=[GlobalException, requests.Response])
        def getFormattedAdditionalMessage(self, globalException, clientResponse):
            responseStatus = HttpStatus.map(globalException.status if ObjectHelper.isNone(clientResponse) else clientResponse.status_code)
            if globalException.status == responseStatus and globalException.status < HttpStatus.INTERNAL_SERVER_ERROR.enumValue:
                exceptionMessage = globalException.message
            elif responseStatus in [
                HttpStatus.BAD_GATWAY,
                HttpStatus.SERVICE_UNAVAILABLE,
                HttpStatus.NOT_FOUND
            ]:
                exceptionMessage = self.helper.voice.getEnumAsSpeech(HttpStatus.map(responseStatus))
            else:
                exceptionMessage = globalException.logMessage
            if HealthCheckConstant.MAXIMUM_MESSAGE_SIZE < len(exceptionMessage):
                exceptionMessage = str(StringHelper.join(exceptionMessage.split(c.COLON)[-2:], character=c.BLANK))[-HealthCheckConstant.MAXIMUM_MESSAGE_SIZE:]
            return f'{c.DOT_SPACE_CAUSE}{exceptionMessage}'


        @HelperMethod(requestClass=[EnumItem])
        def getEnvironmentResponseKey(self, environment):
            return f'{environment.name}{c.COLON}{environment.apiKey}{c.COLON}{environment.apiName}'
