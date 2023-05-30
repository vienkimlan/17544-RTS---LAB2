# from Scheduler.task import *
from scheduler import *
import time

from task1 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1()

scheduler.SCH_Add_Task(task1.Task_Run, 1000, 5000)


while (True):
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1) 

