

class Job():
    
    arrival_time = 0
    absolute_deadline = 0
    execution_time = 0
    executing = False
    remaining_exec_time = 0
    priority = 0
    late = False

    def __init__(self, arrival_time, execution_time, period, priority, executing=False):
        self.arrival_time = arrival_time
        self.absolute_deadline = arrival_time + period
        self.execution_time = execution_time
        self.executing = executing
        self.priority = priority
        self.remaining_exec_time = execution_time

    def progress_job(self):
        if self.executing:
            self.remaining_exec_time -= 1

    def job_complete(self):
        return True if self.remaining_exec_time == 0 else False

    def is_job_late(self, time):
        return True if time > self.absolute_deadline else False

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

    # def __repr__(self):
    #     return "priority of this job" % (self.priority)

    # def __str__(self):
    #     return "priority of this job" % (self.priority)
        
    