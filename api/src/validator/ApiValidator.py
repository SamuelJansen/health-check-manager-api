from python_helper import Constant as c
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus

from dto import ApiDto
from model import Api

@Validator()
class ApiValidator:

    @ValidatorMethod(requestClass=[[ApiDto.ApiRequestDto]])
    def validateRequestDtoList(self, dtoList):
        if self.service.api.existsByKeyIn([dto.key for dto in dtoList]):
            raise GlobalException(message=f'Some Apis already exists', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[ApiDto.ApiRequestDto])
    def validatePostRequestDto(self, dto):
        self.notExistsByKey(dto.key)

    @ValidatorMethod(requestClass=[ApiDto.ApiRequestDto])
    def validatePutRequestDto(self, dto):
        self.existsByKey(dto.key)

    @ValidatorMethod(requestClass=[str])
    def notExistsByKey(self, key):
        self.validator.common.strNotNull(key, 'key')
        if self.service.api.existsByKey(key) :
            raise GlobalException(message=f'Api already exists. Key : {c.SINGLE_QUOTE}{key}{c.SINGLE_QUOTE}', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[str])
    def existsByKey(self, key):
        self.validator.common.strNotNull(key, 'key')
        if not self.service.api.existsByKey(key) :
            raise GlobalException(message=f'''Api does not exists. Key : {c.SINGLE_QUOTE}{key}{c.SINGLE_QUOTE}''', status=HttpStatus.BAD_REQUEST)
