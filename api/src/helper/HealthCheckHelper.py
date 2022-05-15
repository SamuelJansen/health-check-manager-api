from python_helper import Constant as c
from python_helper import log, StringHelper
from python_framework import Helper, HelperMethod, EnumItem, GlobalException, HttpStatus, EnumItem

from constant import HealthCheckConstant


@Helper()
class HealthCheckHelper:

        @HelperMethod(requestClass=[EnumItem, GlobalException])
        def getFormattedErrorMessage(self, environment, globalException):
            formatedAdditionalMessage = self.getFormattedAdditionalMessage(globalException)
            return f'{environment.apiName} {environment.name.lower()} environment is down{formatedAdditionalMessage}'


        @HelperMethod(requestClass=[GlobalException])
        def getFormattedAdditionalMessage(self, globalException):
            if globalException.status < HttpStatus.INTERNAL_SERVER_ERROR:
                exceptionMessage = globalException.message
            elif globalException.status in [
                HttpStatus.BAD_GATWAY,
                HttpStatus.SERVICE_UNAVAILABLE
            ]:
                exceptionMessage = StringHelper.toTitle(HttpStatus.map(globalException.status).enumName.lower().split(c.UNDERSCORE))
            else:
                exceptionMessage = globalException.logMessage
            if HealthCheckConstant.MAXIMUM_MESSAGE_SIZE < len(exceptionMessage):
                exceptionMessage = str(StringHelper.join(exceptionMessage.split(c.COLON)[-2:], character=c.BLANK))[-HealthCheckConstant.MAXIMUM_MESSAGE_SIZE:]
            return f'{c.DOT_SPACE_CAUSE}{exceptionMessage}'


        @HelperMethod(requestClass=[EnumItem])
        def getEnvironmentResponseKey(self, environment):
            return f'{environment.name}{c.COLON}{environment.apiKey}{c.COLON}{environment.apiName}'
