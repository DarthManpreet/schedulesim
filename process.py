class Process (object):

	def __init__(self, pid, priority, start_time, end_time, timer, functionTodo):

		self.id = pid
		self.priority = priority

		# flags state
		self.state = {'ready': False, 'blocked': False, 'running': False}

		# metrics 
		self.start_time = 0
		self.end_time = 0
		self.timer = 0

		# function that a process will execute
		self.functionality = functionTodo

	def __str__(self):
		return "Process ID - {}, Process priority - {}, Process State - {}, Start time - {}, End time - {}".format(self.id, self.priority, self.state, self.start_time, self.end_time)

	def getPid(self):
		return self.pid

	def setPid(self, pid):
		self.pid = pid

	def getPriority(self):
		return self.priority

	def setPriority(self, p):
		self.priority = p

	def set_startTime(self, time):
		self.start_time = time

	def set_endTime(self, time):
		self.end_time = time

	def launchProcess(self):
		return self.functionality(self.id, self.priority, self.start_time, self.end_time, self.state)

def readFile(file):
	with open(file, 'r') as f:
		print(f.read())

# an example usage, it can be substituted with other function calls. - NEEDS END TO END TESTING. 
process = Process(1, "High", 0, 5, 0, readFile('carseats.csv'))



