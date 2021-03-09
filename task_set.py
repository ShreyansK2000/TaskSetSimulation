from collections import namedtuple
import numpy as np
import math

# Immutable task tuple, equivalent to something like a struct in C if it was immutable
Task = namedtuple("Task", ['Period', 'WCET', 'Utilization'])

# logU(a, b) ~ exp(U(log(a), log(b))
def lognuniform(low=1, high=6, base=10):
    return np.power(base, np.random.uniform(low, high, None))

def getTaskSet(utilization_vector, utilization):
    task_set = []
    for i in range(len(utilization_vector)):

        # FOR RTA run, don't need integer period and execution time
        # Different log uniform parameters
        # period = lognuniform(1, 6, 10)
        # wcet = utilization_vector[i] * period * utilization

        # FOR Simulation, need integer values for period and execution time
        period = math.floor(lognuniform(1, 5, 10))
        wcet = math.floor(utilization_vector[i] * period * utilization)

        task_set.append(Task(Period=period, WCET=wcet, Utilization=utilization_vector[i] * utilization))

    # See actual utilization by uncommenting this. Make sure few tasks per task, otherwise too many prints
    # print("utilization ", sum(float(task.WCET)/float(task.Period) for task in task_set))
    return task_set