from python_framework import Controller, ControllerMethod, HttpStatus

from dto import EnvironmentDto


@Controller(url = '/status', tag='Status', description='Status controller')
class StatusAllController:

    @ControllerMethod(url = '/all',
        responseClass = [dict]
    )
    def get(self):
        return self.service.healthCheck.checkAll(), HttpStatus.OK
