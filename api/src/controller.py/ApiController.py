from python_framework import Controller, ControllerMethod, HttpStatus

from dto import ApiDto

@Controller(url = '/apis/all', tag='Api', description='Api controller')
class ApiBatchController:

    @ControllerMethod(
        requestParamClass = [ApiDto.ApiRequestParamDto],
        responseClass = [[ApiDto.ApiResponseDto]]
    )
    def get(self, params=None):
        return self.service.api.findAllByQuery(params), HttpStatus.OK
