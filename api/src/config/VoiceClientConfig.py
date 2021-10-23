from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

BASE_URL = globalsInstance.getSetting('ai-voice-api.base-url')
DEFAULT_TIMEOUT_IN_SECONDS = globalsInstance.getSetting('ai-voice-api.default-timeout-in-seconds')
