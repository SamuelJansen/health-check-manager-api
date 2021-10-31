from python_helper import log
from python_framework import Scheduler, SchedulerMethod, SchedulerType

from config import HealthCheckConfig

@Scheduler()
class HealthCheckScheduler :

    @SchedulerMethod(SchedulerType.INTERVAL, minutes=HealthCheckConfig.HEALTH_CHECK_SCHEDULER_INTERVAL_IN_MINUTES, instancesUpTo=2)
    def check(self) :
        self.service.healthCheck.checkAll()
