from python_helper import ObjectHelper, StringHelper
from python_framework import Service, ServiceMethod, EnumItem, Serializer

from dto import ApiDto
from model import Api


@Service()
class ApiService :

    @ServiceMethod(requestClass=[[ApiDto.ApiRequestDto]])
    def createAll(self, dtoList) :
        self.validator.api.validateCreateRequestDtoList(dtoList)
        modelList = self.mapper.api.fromRequestDtoListToModelList(dtoList)
        self.repository.api.saveAll(modelList)
        return self.mapper.api.fromModelListToResponseDtoList(modelList)

    @ServiceMethod(requestClass=[ApiDto.ApiRequestDto])
    def create(self, dto):
        return self.createAll([dto]).pop()

    @ServiceMethod(requestClass=[ApiDto.ApiRequestParamDto])
    def findAllByQuery(self, query):
        return self.mapper.api.fromModelListToResponseDtoList(self.repository.api.findAllByQuery(Serializer.getObjectAsDictionary(query)))

    @ServiceMethod(requestClass=[str])
    def findByEnvironmentKey(self, environmentKey) :
        return self.mapper.api.fromModelToResponseDto(self.repository.api.findByEnvironmentKey(environmentKey))

    @ServiceMethod(requestClass=[str])
    def findAllByKey(self, key) :
        return self.mapper.api.fromModelListToResponseDtoList(self.repository.api.findAllByKey(key))

    @ServiceMethod(requestClass=[str])
    def findAllByEnvironment(self, environment) :
        return self.mapper.api.fromModelListToResponseDtoList(self.repository.api.findAllByEnvironment(environment)) ###-

    @ServiceMethod(requestClass=[str, str])
    def findByKeyAndEnvironment(self, key, environment) :
        self.validator.api.validateIsUniqueKeyAndEnvironment(key, environment)  ###-
        return self.mapper.api.fromModelToResponseDto(self.repository.api.findByKeyAndEnvironment(key, environment))

    @ServiceMethod(requestClass=[str, str])
    def findAllByKeyAndEnvironment(self, key, environment) :
        return self.mapper.api.fromModelListToResponseDtoList(self.repository.api.findAllByKeyAndEnvironment(key, environment))

    @ServiceMethod()
    def findAll(self) :
        return self.mapper.api.fromModelListToResponseDtoList(self.repository.api.findAll())

    @ServiceMethod(requestClass=[[str]])
    def existsByKeyIn(self, keyList):
        return self.repository.api.existsByKeyIn(keyList)

    @ServiceMethod(requestClass=[[str]])
    def notExistsByEnvironmentKeyIn(self, environmentKeyList):
        return not self.existsByEnvironmentKeyIn(self, environmentKeyList)

    @ServiceMethod(requestClass=[[str]])
    def existsByEnvironmentKeyIn(self, environmentKeyList):
        return self.repository.api.existsByEnvironmentKeyIn(environmentKeyList)

    @ServiceMethod(requestClass=[[str]])
    def notExistsByEnvironmentKeyIn(self, keyList):
        return not self.existsByEnvironmentKeyIn(self, keyList)

    @ServiceMethod(requestClass=[str])
    def existsByEnvironmentKey(self, environmentKey):
        return self.repository.api.existsByEnvironmentKey(environmentKey)

    @ServiceMethod(requestClass=[str, str])
    def existsByKeyAndEnvironment(self, key, environment):
        return self.repository.api.existsByKeyAndEnvironment(key, environment)
