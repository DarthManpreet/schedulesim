from collections import deque
from schedulers import base
from defines import COMPLETE
from defines import INCOMPLETE
from rbt import RedBlackTree
import sys
import math

"""
#====================================================
Completely Fair Scheduler #2

Similar to the first CFS using the RBT, this aims
to select processes that have a low virtual-
runtime (process.counter). This implementation
simply uses a single deque collection to store
processes.

Each time an interrupt occurs, a new process is
retrieved from the ready list having the lowest 
runtime.

Additionally, it utilizes priority levels for a 
process to determine how long the next process will
run before an interrupt is encountered. To determine
the amount of time a process will run, first a
bounded taret amount is found based on its priority.
Then that amount is divided by the total number of
runnable tasks.

process runtime = priority weight / size of readyList

Once this is found, the simulator interrupt value is
changed, guaranteeing the process will not run for
too long.

https://tampub.uta.fi/bitstream/handle/10024/96864/GRADU-1428493916.pdf
#====================================================
"""

class CFS(base.BaseScheduler):
    #==============================================
    #Intialize the red black tree for CFS
    #Params:
    #   processQ = Deque of processes to run
    #   timerInterrupt = Allows scheduler to check
    #                    on running process and to
    #                    make decisions
    #Return:
    #   None
    #==============================================
    def __init__(self, processQ, timerInterrupt):
        super().__init__(processQ, timerInterrupt)
        self.readyList = deque([])
        self.time_minimum = 3
        self.time_high = timerInterrupt
        self.time_low = math.floor(timerInterrupt / 2)
    
    #==============================================
    #Checks to see if the tree is empty
    #Params:
    #   None
    #Return:
    #   Boolean indiciating if tree is empty or
    #   not
    #==============================================
    def empty(self):
        return len(self.readyList) == 0

    #==============================================
    #Add a process to the red black tree
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    def addProcess(self, process):
        if process is not None:
            self.readyList.append(process)


    def readyListPop(self):
        try:
            return self.readyList.pop()
        except IndexError:
            return None

    #==============================================
    #Get the next process to run from the list with
    #the lowest runtime (process.counter)
    #Params:
    #   None
    #Return:
    #   Process with shortest runtime
    #   None if no process in queue
    #==============================================
    def removeProcess(self):
        vruntime = sys.maxsize
        shift = 0
        for i in range (0, len(self.readyList)):
            if self.readyList[i].getProcessRuntime() < vruntime:
                vruntime = self.readyList[i].getProcessRuntime()
                shift = i
        self.readyList.rotate(shift-1)
        return self.readyListPop()
  
    #==============================================
    #Get the next process for the scheduler to run.
    #Using the process's priority and the number of
    #runnable processes, determine how long this
    #process will run.
    #This implements the scheduler heuristics.
    #Params:
    #   curProc = Current process that's running on
    #             scheduler
    #Return:
    #   Next process in the queue via call to 
    #   removeProcess()
    #==============================================
    def getNext(self, curProc):
        extraProc = 1
        if curProc is not None:
            extraProc = 2
        # get the next process to run
        nextProc = self.removeProcess()
        # calculate time new proc can run
        if nextProc is not None:
            time = 0
            # set interrupt using this time
            if nextProc.getPriority() == "High":
                time = self.time_high /(len(self.readyList)+extraProc)
            else:
                time = self.time_low /(len(self.readyList)+extraProc)

            if time < self.time_minimum:
                self.timerInterrupt = self.time_minimum
            else:
                self.timerInterrupt = math.floor(time)

        if curProc is not None and curProc.get_status() != COMPLETE:
            self.readyList.append(curProc)
        return nextProc
