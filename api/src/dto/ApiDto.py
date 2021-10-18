from python_framework import ConverterStatic

from enumeration.ApiType import ApiType
from enumeration.ApiEnvironment import ApiEnvironment
from constant import ApiConstant

class ApiRequestDto:
    def __init__(self,
        key = None,
        host = None,
        type = None,
        environment = None,
        name = None
    ):
        self.key = key
        self.host = host
        self.type = ApiType.map(ConverterStatic.getValueOrDefault(type, ApiConstant.DEFAULT_API_TYPE))
        self.environment = ApiEnvironment.map(ConverterStatic.getValueOrDefault(environment, ApiConstant.DEFAULT_API_ENVIRONMENT))
        self.name = name

class ApiResponseDto:
    def __init__(self,
        key = None,
        host = None,
        type = None,
        environment = None,
        name = None
    ):
        self.key = key
        self.host = host
        self.type = ApiType.map(type)
        self.environment = ApiEnvironment.map(environment)
        self.name = name
