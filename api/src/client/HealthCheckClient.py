import requests
from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from python_framework import HttpClient, HttpClientMethod, HttpStatus, GlobalException

from config import HealthCheckConfig


@HttpClient(
    timeout = HealthCheckConfig.CLIENT_CHECK_REQUEST_TIME_OUT_IN_SECONDS
)
class HealthCheckClient :

    @HttpClientMethod(requestClass=[str], returnOnlyBody=False)
    def checkHealth(self, url) :
        return self.get(additionalUrl=url)
