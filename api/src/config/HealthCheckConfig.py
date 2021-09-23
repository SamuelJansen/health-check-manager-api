from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

HEALTH_CHECK_SCHEDULER_TIME_IN_MINUTES = int(globalsInstance.getApiSetting('health-check.sheduler.health-check.time-in-minutes'))
CLIENT_CHECK_REQUEST_TIME_OUT_IN_SECONDS = int(globalsInstance.getApiSetting('health-check.sheduler.health-check.client.timeout-in-seconds'))
