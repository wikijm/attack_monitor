from .feeder import *
from stone_engine import evtx_subscriber
from feeders.structures import *
from utils.nicedate import NiceDate

class feeder_evtx_task_scheduler(Feeder):

    def getName(self):
        return 'evtx_task_scheduler'

    def run(self):
        for er in evtx_subscriber.subscribe_and_yield_events('Microsoft-Windows-TaskScheduler/Operational'):
            pass_mq = mq(er, TYPE_LOG_EVENT, self.getName(), NiceDate.log_event_to_nice_date(er), generate_mq_key(er, self.getName()), None)
            self.add_to_ultra_mq(pass_mq)
            self.global_break()
