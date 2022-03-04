from python_framework import ConverterStatic

from constant import EnvironmentConstant

class EnvironmentRequestDto:
    def __init__(self,
        key = None,
        name = None,
        apiKey = None,
        healthUrl = None,
        apiName = None
    ):
        self.key = key
        self.name = ConverterStatic.getValueOrDefault(name, EnvironmentConstant.DEFAULT_ENVIRONMENT_NAME)
        self.apiKey = apiKey
        self.healthUrl = healthUrl
        self.apiName = apiName

class EnvironmentResponseDto:
    def __init__(self,
        key = None,
        name = None,
        apiKey = None,
        healthUrl = None,
        apiName = None
    ):
        self.key = key
        self.name = name
        self.apiKey = apiKey
        self.healthUrl = healthUrl
        self.apiName = apiName

class ApiRequestParamDto:
    def __init__(self,
        name = None,
        apiKey = None
    ):
        self.name = name
        self.apiKey = apiKey
