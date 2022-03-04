from python_helper import ObjectHelper, StringHelper
from python_framework import Service, ServiceMethod, EnumItem, Serializer

from dto import EnvironmentDto
from model import Environment


@Service()
class EnvironmentService :

    @ServiceMethod(requestClass=[[EnvironmentDto.EnvironmentRequestDto]])
    def createAll(self, dtoList) :
        self.validator.environment.validateCreateRequestDtoList(dtoList)
        modelList = self.mapper.environment.fromRequestDtoListToModelList(dtoList)
        self.repository.environment.saveAll(modelList)
        return self.mapper.environment.fromModelListToResponseDtoList(modelList)

    @ServiceMethod(requestClass=[EnvironmentDto.EnvironmentRequestDto])
    def create(self, dto):
        return self.createAll([dto]).pop()

    @ServiceMethod(requestClass=[EnvironmentDto.ApiRequestParamDto])
    def findAllByQuery(self, query):
        return self.mapper.environment.fromModelListToResponseDtoList(self.repository.environment.findAllByQuery(Serializer.getObjectAsDictionary(query)))

    @ServiceMethod(requestClass=[str])
    def findByKey(self, key):
        model = self.repository.environment.findByKey(key)
        self.validator.environment.validateIsFound(model, key)
        return self.mapper.environment.fromModelToResponseDto()

    @ServiceMethod(requestClass=[str])
    def findAllByApiKey(self, apiKey) :
        return self.mapper.environment.fromModelListToResponseDtoList(self.repository.environment.findAllByApiKey(apiKey))

    @ServiceMethod(requestClass=[str])
    def findAllByName(self, name) :
        return self.mapper.environment.fromModelListToResponseDtoList(self.repository.environment.findAllByName(name)) ###-

    @ServiceMethod(requestClass=[str, str])
    def findByApiKeyAndName(self, apiKey, name) :
        self.validator.environment.validateIsUniqueKeyAndName(apiKey, name)  ###-
        return self.mapper.environment.fromModelToResponseDto(self.repository.environment.findByApiKeyAndName(apiKey, name))

    @ServiceMethod(requestClass=[str, str])
    def findAllByApiKeyAndName(self, apiKey, name) :
        return self.mapper.environment.fromModelListToResponseDtoList(self.repository.environment.findAllByApiKeyAndName(apiKey, name))

    @ServiceMethod()
    def findAll(self) :
        return self.mapper.environment.fromModelListToResponseDtoList(self.repository.environment.findAll())

    @ServiceMethod(requestClass=[[str]])
    def existsByApiKeyIn(self, apiKeyList):
        return self.repository.environment.existsByApiKeyIn(apiKeyList)

    @ServiceMethod(requestClass=[[str]])
    def notExistsByApiKeyIn(self, keyList):
        return not self.existsByApiKeyIn(self, keyList)

    @ServiceMethod(requestClass=[[str]])
    def existsByKeyIn(self, keyList):
        return self.repository.environment.existsByKeyIn(keyList)

    @ServiceMethod(requestClass=[[str]])
    def notExistsByKeyIn(self, apiKeyList):
        return not self.existsByKeyIn(self, apiKeyList)

    @ServiceMethod(requestClass=[str])
    def existsByKey(self, key):
        return self.repository.environment.existsByKey(key)

    @ServiceMethod(requestClass=[str, str])
    def existsByApiKeyAndName(self, apiKey, name):
        return self.repository.environment.existsByApiKeyAndName(apiKey, name)
