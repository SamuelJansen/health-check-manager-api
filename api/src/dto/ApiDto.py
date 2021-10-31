from python_framework import ConverterStatic

from constant import ApiConstant

class ApiRequestDto:
    def __init__(self,
        environmentKey = None,
        environment = None,
        key = None,
        healthUrl = None,
        name = None
    ):
        self.environmentKey = environmentKey
        self.environment = ConverterStatic.getValueOrDefault(environment, ApiConstant.DEFAULT_API_ENVIRONMENT)
        self.key = key
        self.healthUrl = healthUrl
        self.name = name

class ApiResponseDto:
    def __init__(self,
        environmentKey = None,
        environment = None,
        key = None,
        healthUrl = None,
        name = None
    ):
        self.environmentKey = environmentKey
        self.environment = environment
        self.key = key
        self.healthUrl = healthUrl
        self.name = name

class ApiRequestParamDto:
    def __init__(self,
        environment = None,
        key = None
    ):
        self.environment = environment
        self.key = key
