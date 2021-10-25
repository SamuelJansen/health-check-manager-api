from python_framework import Enum, EnumItem

@Enum()
class ApiEnvironmentEnumeration :
    INTERNAL = EnumItem()
    DEVELOPMENT = EnumItem()
    HOMOLOGATION = EnumItem()
    PRODUCTION = EnumItem()
    NONE = EnumItem()

ApiEnvironment = ApiEnvironmentEnumeration()
