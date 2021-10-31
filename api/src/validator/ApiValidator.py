from python_helper import Constant as c
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus

from dto import ApiDto
from model import Api

@Validator()
class ApiValidator:

    @ValidatorMethod(requestClass=[[ApiDto.ApiRequestDto]])
    def validateCreateRequestDtoList(self, dtoList):
        for dto in dtoList:
            if self.service.api.existsByKeyAndEnvironment(dto.key, dto.environment):
                raise GlobalException(message=f'Api with key: {dto.key} and enveironment: {dto.environment} already exists', status=HttpStatus.BAD_REQUEST)
        if self.service.api.existsByEnvironmentKeyIn([dto.environmentKey for dto in dtoList]):
            raise GlobalException(message=f'Some Apis already exists. Environment keys: {[dto.environmentKey for dto in dtoList]}', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[ApiDto.ApiRequestDto])
    def validatePostRequestDto(self, dto):
        self.notExistsByEnvironmentKeyIn(dto.environmentKey)

    @ValidatorMethod(requestClass=[ApiDto.ApiRequestDto])
    def validatePutRequestDto(self, dto):
        self.existsByKey(dto.environmentKey)

    @ValidatorMethod(requestClass=[str])
    def notExistsByEnvironmentKeyIn(self, environmentKey):
        self.validator.common.strNotNull(environmentKey, 'environmentKey')
        if self.service.api.existsByEnvironmentKey(key) :
            raise GlobalException(message=f'Api already exists with environmentKey : {c.SINGLE_QUOTE}{environmentKey}{c.SINGLE_QUOTE}', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[str])
    def existsByKey(self, environmentKey):
        self.validator.common.strNotNull(environmentKey, 'environmentKey')
        if not self.service.api.existsByKey(environmentKey) :
            raise GlobalException(message=f'''Api does not exists with environmentKey : {c.SINGLE_QUOTE}{environmentKey}{c.SINGLE_QUOTE}''', status=HttpStatus.BAD_REQUEST)
