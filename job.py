

class Job():
    
    arrival_time = 0
    absolute_deadline = 0
    execution_time = 0
    executing = False
    remaining_exec_time = 0
    priority = 0

    def __init__(self, arrival_time, execution_time, priority, executing=False):
        self.arrival_time = arrival_time
        self.absolute_deadline = arrival_time + execution_time
        self.execution_time = execution_time
        self.executing = executing
        self.priority
        self.remaining_exec_time = execution_time

    def progress_job(self):
        if self.executing:
            self.remaining_exec_time -= 1

    def start_job(self, time):
        self.remaining_exec_time = self.execution_time
        self.executing = True
        self.absolute_deadline = time + self.execution_time

    def pause_job(self):
        self.executing = False

    def resume_job(self):
        if not self.executing:
            self.executing = True

    def deadline_missed(self, time):
        return time > self.absolute_deadline
        