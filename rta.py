import math
import numpy as np

def RTASchedulable(priority_sorted_task_set):

    for i, task in enumerate(priority_sorted_task_set):

        tau_i = task
        schedulable = 0

        # For first iteration interference is the sum of HP execution times
        interference = sum(task.WCET for task in priority_sorted_task_set[:i])

        while schedulable == 0:
            
            # R_i^n
            response_time = tau_i.WCET + interference

            if response_time > tau_i.Period:  # Since we're considering implicit deadlines, check period      
                return 0
            
            # Interference is the ceiling of the number of interruptions from higher priority tasks during execution
            interference = sum(math.ceil(float(response_time) / float(tau_k.Period)) * tau_k.WCET for tau_k in priority_sorted_task_set[:i])
            # for k in range(i):
            #     tau_k = priority_sorted_task_set[k]
            #     interference += math.ceil(float(response_time) / float(tau_k.Period)) * tau_k.WCET

            if interference + tau_i.WCET <= response_time:
                schedulable = 1

    return 1

def RM_RTA_Schedulable(task_set):

    # Check Hyperbolic bound, faster than RTA
    if np.prod([(task.Utilization + 1) for task in task_set]) <= 2:
        return 1

    # Sort tasks with ascending order of periods
    task_set.sort(key=lambda task: task.Period)
    return RTASchedulable(task_set)

def SPTF_RTA_Schedulable(task_set):
    # Sort tasks with ascending order of execution times
    task_set.sort(key=lambda task: task.WCET)
    return RTASchedulable(task_set)

def MUF_RTA_Schedulable(task_set):
    # Sort tasks with descending order of utilization
    task_set.sort(key=lambda task: task.Utilization, reverse=True)
    return RTASchedulable(task_set)