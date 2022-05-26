import requests
from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from queue_manager_api import MessageEmitter, MessageEmitterMethod
from python_framework import HttpStatus, GlobalException, JwtConstant

from config import QueueConfig, NotificationConfig


@MessageEmitter(
    url = QueueConfig.API_NOTIFICATIONS_EMITTER_BASE_URL,
    headers = {
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {QueueConfig.API_NOTIFICATIONS_EMITTER_API_KEY}'
    },
    timeout = QueueConfig.API_NOTIFICATIONS_EMITTER_TIMEOUT,
)
class NotificationEmitter :

    @MessageEmitterMethod(
        queueKey = QueueConfig.API_NOTIFICATIONS_QUEUE_KEY,
        requestClass=[[dict]]
    )
    def notifyAll(self, dtoList):
        return self.emit(
            messageHeaders = {
                JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {NotificationConfig.API_KEY}'
            }
            body = dtoList
        )
