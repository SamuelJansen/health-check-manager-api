from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

HEALTH_CHECK_SCHEDULER_INTERVAL_IN_MINUTES = int(globalsInstance.getApiSetting('health-check.sheduler.health-check.interval-in-minutes'))
CLIENT_CHECK_REQUEST_TIME_OUT_IN_SECONDS = globalsInstance.getApiSetting('health-check.sheduler.health-check.client.timeout-in-seconds')
