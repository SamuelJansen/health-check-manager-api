from python_helper import Constant as c
from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus

from dto import EnvironmentDto
from model import Environment

@Validator()
class EnvironmentValidator:

    @ValidatorMethod(requestClass=[[EnvironmentDto.EnvironmentRequestDto]])
    def validateUpdateRequestDtoList(self, dtoList):
        for dto in dtoList:
            if self.service.environment.notExistsByApiKeyAndName(dto.apiKey, dto.name):
                raise GlobalException(message=f'Api with key "{dto.apiKey}" and environment "{dto.name}" does not exists', status=HttpStatus.BAD_REQUEST)
        if self.service.environment.notExistsByKeyIn([dto.key for dto in dtoList]):
            raise GlobalException(message=f'Some Environments does not exists. Environment keys: {[dto.key for dto in dtoList]}', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[[EnvironmentDto.EnvironmentRequestDto]])
    def validateCreateRequestDtoList(self, dtoList):
        for dto in dtoList:
            if self.service.environment.existsByApiKeyAndName(dto.apiKey, dto.name):
                raise GlobalException(message=f'Api with key "{dto.apiKey}" and environment "{dto.name}" already exists', status=HttpStatus.BAD_REQUEST)
        if self.service.environment.existsByKeyIn([dto.key for dto in dtoList]):
            raise GlobalException(message=f'Some Environments already exists. Environment keys: {[dto.key for dto in dtoList]}', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[EnvironmentDto.EnvironmentRequestDto])
    def validatePostRequestDto(self, dto):
        self.notExistsByKeyIn(dto.key)

    @ValidatorMethod(requestClass=[Environment.Environment, str])
    def validateIsFound(self, model, key):
        if ObjectHelper.isNone(model) or not model.key == key:
            raise GlobalException(message=f'''Environment '{key}' not found''', status=HttpStatus.NOT_FOUND)

    @ValidatorMethod(requestClass=[EnvironmentDto.EnvironmentRequestDto])
    def validatePutRequestDto(self, dto):
        self.existsByKey(dto.key)

    @ValidatorMethod(requestClass=[str])
    def notExistsByKeyIn(self, key):
        self.validator.common.strNotNull(key, 'key')
        if self.service.environment.existsByKey(key) :
            raise GlobalException(message=f'Environment already exists with key : {c.SINGLE_QUOTE}{key}{c.SINGLE_QUOTE}', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[str])
    def existsByKey(self, key):
        self.validator.common.strNotNull(key, 'key')
        if not self.service.environment.existsByKey(key) :
            raise GlobalException(message=f'''Environment does not exists with key : {c.SINGLE_QUOTE}{key}{c.SINGLE_QUOTE}''', status=HttpStatus.BAD_REQUEST)
