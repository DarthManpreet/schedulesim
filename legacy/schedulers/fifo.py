from collections import deque
from process import Process
"""
#==================================================
First In First Out

The idea behind this scheduling algorithm is that
tasks are scheduled in the order that they are
added in the queue. The process is executed till it
is completed or it's given up the CPU. The downside
with this is that this algorithm is nonpreemptive,
which means that short processes which are in the 
back of queue will have to wait for long process at
front to finish. 
#==================================================
"""
class FIFO():
    #==============================================
    #Intialize the run queue for FIFO
    #Params:
    #   None
    #Return:
    #   None
    #==============================================
    def __init__(self):
        self.runQueue = deque([])

    # reorders process list based on arrival time for the scheduler
    # to pick up a single process. 

    def procSort(self, proc_list):
        for idx in range(0, len(proc_list) - 1):
            if proc_list[idx].get_startTime() > proc_list[idx + 1].get_startTime():
                temp = proc_list[idx]
                proc_list[idx] = proc_list[idx + 1]
                proc_list[idx + 1] = temp
        return proc_list # updated list. 

    
    #==============================================
    #Add a process to the end of the run queue
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    def addProcess(self, process):
        self.runQueue.append(process)
    
    #==============================================
    #Get the next process on the queue
    #Params:
    #   None
    #Return:
    #   Next process on the queue
    #   None if no process in queue
    #==============================================
    def getNextProcess(self):
        try:
            return self.runQueue.popleft()
        except IndexError:
            return None
    
    #==============================================
    #Run the scheduler through all the processes
    #Params:
    #   None
    #Return:
    #   None
    #==============================================
    def run(self):
        #While there's process in the queue
        while self.runQueue:
            #Get process to run
            toRun = self.getNextProcess()

            #TODO: Run process till completion
            toRun.launchProcess()
