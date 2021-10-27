from python_framework import ConverterStatic

from constant import ApiConstant

class ApiRequestDto:
    def __init__(self,
        key = None,
        healthUrl = None,
        environment = None,
        name = None
    ):
        self.key = key
        self.healthUrl = healthUrl
        self.environment = ConverterStatic.getValueOrDefault(environment, ApiConstant.DEFAULT_API_ENVIRONMENT)
        self.name = name

class ApiResponseDto:
    def __init__(self,
        key = None,
        healthUrl = None,
        environment = None,
        name = None
    ):
        self.key = key
        self.healthUrl = healthUrl
        self.environment = environment
        self.name = name
