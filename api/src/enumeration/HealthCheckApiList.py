from python_framework import Enum, EnumItem

from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

@Enum()
class HealthCheckApiListEnumeration :
    # SPEECH_API = EnumItem(url=globalsInstance.getSetting('speech-api.base-url'))
    # RIACHUELO_AUTOMATING_API = EnumItem(url=globalsInstance.getSetting('riachuelo-automating-api.base-url'))
    # NGROK_MANAGER_API = EnumItem(url=globalsInstance.getSetting('ngrok-manager-api.base-url'))
    # IDEALIZAR_AGENDA_API = EnumItem(url=globalsInstance.getSetting('idealizar.agenda-api.base-url'))
    # IDEALIZAR_WHATS_APP_WEB_API = EnumItem(url=globalsInstance.getSetting('idealizar.whats-app.web-api.base-url'))
    # IDEALIZAR_WHATS_APP_MANAGER_API = EnumItem(url=globalsInstance.getSetting('idealizar.whats-app.manager-api.base-url'))
    ...

HealthCheckApiList = HealthCheckApiListEnumeration()
