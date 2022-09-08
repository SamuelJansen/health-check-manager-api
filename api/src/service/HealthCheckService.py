import requests

from python_helper import Constant as c
from python_helper import log, StringHelper, ObjectHelper
from python_framework import Service, ServiceMethod, GlobalException, HttpStatus, EnumItem, HttpDomain, FlaskUtil, ActuatorHealthStatus
from notification_manager_api import NotificationDestiny

from constant import HealthCheckConstant


@Service()
class HealthCheckService :

    @ServiceMethod()
    def checkAll(self) :
        reponseDictionary = {}
        for environment in self.service.environment.findAll():
            response = {}
            responseStatus = HttpStatus.INTERNAL_SERVER_ERROR
            formatedAdditionalMessage = f'{c.BLANK}'
            errorNotificationMessage = HealthCheckConstant.DEFAULT_ERROR_NOTIFICATION_MESSAGE
            try:
                response, responseHeader, responseStatus = self.client.healthCheck.checkHealth(f'{environment.healthUrl}')
            except GlobalException as globalException:
                clientResponse = globalException.logPayload.get(HttpDomain.RESPONSE_BODY_KEY, {}).get(FlaskUtil.CLIENT_RESPONSE)
                log.failure(self.checkAll, 'Not possible to check environment', exception=globalException, muteStackTrace=True)
                response = {
                    'status': ActuatorHealthStatus.DOWN,
                    'message': globalException.message,
                    'logMessage': globalException.logMessage,
                    'debug': c.BLANK if ObjectHelper.isNone(clientResponse) else clientResponse.text
                }
                errorNotificationMessage = self.helper.healthCheck.getFormattedErrorMessage(environment, globalException, clientResponse)
            reponseDictionary[self.helper.healthCheck.getEnvironmentResponseKey(environment)] = {
                'response': response,
                'status': responseStatus
            }
            if ActuatorHealthStatus.DOWN == response['status']:
                self.notifyError(environment, errorNotificationMessage)
        log.prettyPython(self.checkAll, 'Apis status', reponseDictionary, logLevel=log.STATUS)
        return reponseDictionary


    @ServiceMethod(requestClass=[EnumItem, str])
    def notifyError(self, environment, errorNotificationMessage):
        self.service.notification.notifyErrorTo(
            errorNotificationMessage,
            [NotificationDestiny.TELEGRAM, NotificationDestiny.VOICE]
        )
