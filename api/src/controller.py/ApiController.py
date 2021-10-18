from python_framework import Controller, ControllerMethod, HttpStatus

from dto import ApiDto

@Controller(url = '/api', tag='Api', description='Api controller')
class ApiController:

    @ControllerMethod(url = '/',
        requestClass = [ApiDto.ApiRequestDto],
        responseClass = [ApiDto.ApiResponseDto]
    )
    def post(self, dto):
        return self.service.api.create(dto), HttpStatus.CREATED

@Controller(url = '/api/batch', tag='Api', description='Api controller')
class ApiBatchController:

    @ControllerMethod(url = '/')
    def get(self, dto):
        return self.service.api.findAll(), HttpStatus.CREATED
