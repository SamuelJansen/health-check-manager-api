from python_framework import Controller, ControllerMethod, HttpStatus

from dto import EnvironmentDto

@Controller(url = '/apis/environments', tag='Environment', description='Environment controller')
class EnvironmentController:

    @ControllerMethod(url = '/<string:key>',
        responseClass = [EnvironmentDto.EnvironmentResponseDto]
    )
    def get(self, key=None):
        return self.service.environment.findByKey(key), HttpStatus.OK

    @ControllerMethod(url = '/',
        requestClass = [EnvironmentDto.EnvironmentRequestDto],
        responseClass = [EnvironmentDto.EnvironmentResponseDto]
    )
    def post(self, dto):
        return self.service.environment.create(dto), HttpStatus.CREATED

@Controller(url = '/apis/environments', tag='Environment', description='Environment controller')
class EnvironmentBatchController:

    @ControllerMethod(url = '/all',
        responseClass = [[EnvironmentDto.EnvironmentResponseDto]]
    )
    def get(self):
        return self.service.environment.findAll(), HttpStatus.OK

    @ControllerMethod(url = '/all',
        requestClass = [[EnvironmentDto.EnvironmentRequestDto]],
        responseClass = [[EnvironmentDto.EnvironmentResponseDto]]
    )
    def post(self, dtoList):
        return self.service.environment.createAll(dtoList), HttpStatus.CREATED
