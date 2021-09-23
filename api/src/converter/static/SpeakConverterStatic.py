from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, EnvironmentHelper
from python_framework import ConverterStatic

from config import SpeechConfig
from domain import SpeechConstants

def fullAudioPathAndNameAndExtension(audioDto) :
    path = f'{audioDto.path}' if ObjectHelper.isNotNone(audioDto.path) and StringHelper.isNotBlank(audioDto.path) else c.BLANK
    osSeparator = f'{EnvironmentHelper.OS_SEPARATOR}' if StringHelper.isNotBlank(path) else c.BLANK
    return f'{path}{osSeparator}{audioDto.name}.{audioDto.extension}'

def getValidName(originalName) :
    if ObjectHelper.isNotNone(originalName) :
        return StringHelper.join([character for character in originalName if character in SpeechConstants.VALID_CHARACTER_SET], character=c.BLANK)

def toRequestDto(dto) :
    dto.extension = ConverterStatic.getValueOrDefault(dto.extension, 'mp3')
    dto.path = ConverterStatic.getValueOrDefault(dto.path, SpeechConfig.SPEECH_STATIC_FILE_PATH)
    if ObjectHelper.isNone(dto.name) and ObjectHelper.isNotNone(dto.text) :
        dto.name = getValidName(dto.text.lower())
