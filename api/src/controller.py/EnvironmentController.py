from python_framework import Controller, ControllerMethod, HttpStatus

from dto import ApiDto

@Controller(url = '/environments', tag='Environment', description='Environment controller')
class EnvironmentController:

    @ControllerMethod(url = '/<string:environmentKey>',
        responseClass = [ApiDto.ApiResponseDto]
    )
    def get(self, environmentKey):
        return self.service.api.findByEnvironmentKey(environmentKey), HttpStatus.OK

    @ControllerMethod(url = '/',
        requestClass = [ApiDto.ApiRequestDto],
        responseClass = [ApiDto.ApiResponseDto]
    )
    def post(self, dto):
        return self.service.api.create(dto), HttpStatus.CREATED

@Controller(url = '/environments', tag='Environment', description='Api controller')
class EnvironmentBatchController:

    @ControllerMethod(url = '/all',
        responseClass = [[ApiDto.ApiResponseDto]]
    )
    def get(self):
        return self.service.api.findAll(), HttpStatus.OK

    @ControllerMethod(url = '/all',
        requestClass = [[ApiDto.ApiRequestDto]],
        responseClass = [[ApiDto.ApiResponseDto]]
    )
    def post(self, dtoList):
        return self.service.api.createAll(dtoList), HttpStatus.CREATED
