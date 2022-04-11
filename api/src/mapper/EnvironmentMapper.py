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

    @MapperMethod(requestClass=[[Environment.Environment], [EnvironmentDto.EnvironmentRequestDto]])
    def overrideModelList(self, modelList, dtoList):
        for model in modelList:
            for dto in dtoList:
                if model.key == dto.key:
                    self.overrideModel(model, dto)
                    break

    @MapperMethod(requestClass=[Environment.Environment, EnvironmentDto.EnvironmentRequestDto])
    def overrideModel(self, model, dto):
        model.name = dto.name
        model.apiKey = dto.apiKey
        model.healthUrl = dto.healthUrl
        model.apiName = dto.apiName
