from collections import namedtuple
import numpy as np
import math

Task = namedtuple("Task", ['Period', 'WCET', 'Utilization'])

# logU(a, b) ~ exp(U(log(a), log(b))
def lognuniform(low=1, high=6, base=10):
    return np.power(base, np.random.uniform(low, high, None))

def getTaskSet(utilization_vector, utilization):
    task_set = []
    for i in range(len(utilization_vector)):
        period = math.floor(lognuniform(1, 5, 10))
        wcet = math.floor(utilization_vector[i] * period * utilization)
        # if wcet == 0:
        #     wcet = 1
            # print("BADDDDDD")
        task_set.append(Task(Period=period, WCET=wcet, Utilization=utilization_vector[i] * utilization))

    # print("utilization ", sum(float(task.WCET)/float(task.Period) for task in task_set))
    return task_set