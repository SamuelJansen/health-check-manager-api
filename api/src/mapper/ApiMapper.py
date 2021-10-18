from python_framework import Mapper, MapperMethod

from dto import ApiDto
from model import Api

@Mapper()
class ApiMapper:

    @MapperMethod(requestClass=[[ApiDto.ApiRequestDto]], responseClass=[[Api.Api]])
    def fromRequestDtoListToModelList(self, dtoList, modelList) :
        return modelList

    @MapperMethod(requestClass=[[Api.Api]], responseClass=[[ApiDto.ApiResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList) :
        return dtoList

    @MapperMethod(requestClass=[ApiDto.ApiRequestDto], responseClass=[Api.Api])
    def fromRequestDtoToModel(self, dto, model) :
        return model

    @MapperMethod(requestClass=[Api.Api], responseClass=[ApiDto.ApiResponseDto])
    def fromModelToResponseDto(self, model, dto) :
        return dto
