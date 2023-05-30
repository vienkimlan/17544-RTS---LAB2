# from Scheduler.task import *
from scheduler import *
import time

from task1 import *
from task2 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1(0)

task2 = Task2(1)

scheduler.SCH_Add_Task(task1.Task_Run, 1000, 5000)
scheduler.SCH_Add_Task(task2.Task_Run, 1000, 5000)

while (True):
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1) 

