from python_framework import Service, ServiceMethod, EnumItem

from dto import ApiDto
from model import Api


@Service()
class ApiService :

    @ServiceMethod(requestClass=[[ApiDto.ApiRequestDto]])
    def createAll(self, dtoList) :
        self.validator.api.validateRequestDtoList(dtoList)
        modelList = self.mapper.api.fromRequestDtoListToModelList(dtoList)
        self.repository.api.saveAll(modelList)
        return self.mapper.api.fromModelListToResponseDtoList(modelList)

    @ServiceMethod(requestClass=[ApiDto.ApiRequestDto])
    def create(self, dto):
        return self.createAll([dto]).pop()

    @ServiceMethod()
    def findAll(self) :
        return self.mapper.api.fromModelListToResponseDtoList(self.repository.api.findAll())

    @ServiceMethod(requestClass=[[str]])
    def existsByKeyIn(self, keyList):
        return self.repository.api.existsByKeyIn(keyList)

    @ServiceMethod(requestClass=[[str]])
    def notExistsByKeyIn(self, keyList):
        return not self.existsByKeyIn(self, keyList)

    @ServiceMethod(requestClass=[str])
    def existsByKey(self, key):
        return self.repository.api.existsByKey(key)
