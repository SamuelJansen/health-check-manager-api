from python_framework import Controller, ControllerMethod, HttpStatus

from dto import EnvironmentDto

@Controller(url = '/apis/all', tag='Environment', description='Environment controller')
class EnvironmentQueryBatchController:

    @ControllerMethod(
        requestParamClass = [EnvironmentDto.ApiRequestParamDto],
        responseClass = [[EnvironmentDto.EnvironmentResponseDto]]
    )
    def get(self, params=None):
        return self.service.environment.findAllByQuery(params), HttpStatus.OK
