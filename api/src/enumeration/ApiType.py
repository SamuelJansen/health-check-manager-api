from python_framework import Enum, EnumItem

@Enum()
class ApiTypeEnumeration :
    AI = EnumItem()
    PERSONAL = EnumItem()
    PUBLIC = EnumItem()
    BUSINESS = EnumItem()
    NONE = EnumItem()

ApiType = ApiTypeEnumeration()
