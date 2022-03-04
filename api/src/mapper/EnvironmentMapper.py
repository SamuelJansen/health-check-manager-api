from python_framework import Mapper, MapperMethod

from dto import EnvironmentDto
from model import Environment

@Mapper()
class EnvironmentMapper:

    @MapperMethod(requestClass=[[EnvironmentDto.EnvironmentRequestDto]], responseClass=[[Environment.Environment]])
    def fromRequestDtoListToModelList(self, dtoList, modelList) :
        return modelList

    @MapperMethod(requestClass=[[Environment.Environment]], responseClass=[[EnvironmentDto.EnvironmentResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList) :
        return dtoList

    @MapperMethod(requestClass=[EnvironmentDto.EnvironmentRequestDto], responseClass=[Environment.Environment])
    def fromRequestDtoToModel(self, dto, model) :
        return model

    @MapperMethod(requestClass=[Environment.Environment], responseClass=[EnvironmentDto.EnvironmentResponseDto])
    def fromModelToResponseDto(self, model, dto) :
        return dto
