from python_helper import log
from python_framework import Scheduler, SchedulerMethod

from config import HealthCheckConfig

@Scheduler()
class HealthCheckScheduler :

    @SchedulerMethod('interval', minutes=HealthCheckConfig.HEALTH_CHECK_SCHEDULER_TIME_IN_MINUTES, instancesUpTo=2)
    def check(self) :
        log.debug(self.check, 'starded')
        self.service.healthCheck.checkAll()
        log.debug(self.check, 'ended')
