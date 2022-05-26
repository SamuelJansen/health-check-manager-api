from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from python_framework import Service, ServiceMethod, EnumItem


@Service()
class NotificationService:

    @ServiceMethod(requestClass=[[str]])
    def notifyAll(self, textList) :
        serviceReturn = None
        try:
            serviceReturn = self.emitter.notification.notifyAll([{'severity': 'STATUS', 'message': text} for text in textList])
        except Exception as exception:
            log.failure(self.notifyAll, 'Not possible to notify all', exception=exception, muteStackTrace=True)
        return serviceReturn


    @ServiceMethod(requestClass=[str])
    def notify(self, text) :
        serviceReturn = None
        try:
            serviceReturn = self.notifyAll([text])
        except Exception as exception:
            log.failure(self.notify, 'Not possible to notify', exception=exception, muteStackTrace=True)
        return serviceReturn
