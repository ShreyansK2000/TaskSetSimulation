from job import Job
import numpy as np
from task_set import *
from random_vector_generator import *
import matplotlib.pyplot as plt

def add_jobs(t, arrived_jobs, task_set):

    for i, task in enumerate(task_set):
        if t % task.Period == 0:
            arrived_jobs.append(Job(t, task.WCET, task.Period, i, executing=False)) 

def Simulation(n, task_set):

    num_time_units = 1000
    num_jobs_started = 0
    num_jobs_completed_in_time = 0
    arrived_jobs = [Job(0, task.WCET, task.Period, i, False) for i, task in enumerate(task_set)]

    #=============Only for DEBUG======================
    i = 1
    for job in arrived_jobs:
        print("job" + str(i) + ' ' + str(job.priority))
        i += 1
    #=================================================

    current_job = None
    for t in range(num_time_units + 1):

        if t > 0:
            # check if new jobs are arriving,
            # add to readyqueue if arrived
            add_jobs(t, arrived_jobs, task_set)

        # Sort the ready queue by job priority (schedule function responsible for this)
        arrived_jobs.sort(key=lambda job: job.priority)         


        # Relevant at t = 0, no starting job
        if current_job is None:
            current_job = arrived_jobs.pop(0)

        # check if next item in ready queue is higher priority
        # semantically: priority(0) > priority(1)
        # but in code, we check for smaller index
        if arrived_jobs[0].priority < current_job.priority:
            current_job.pause_job()
            arrived_jobs.append(current_job)
            current_job = arrived_jobs.pop(0)

        if current_job.executing:
            current_job.progress_job()
            if current_job.job_complete(): 
                if not current_job.is_job_late():
                    num_jobs_completed_in_time += 1

                # start next job at same time instance
                # assume 0 context switching overhead
                current_job = arrived_jobs.pop(0)
                current_job.start_job(t)
                num_jobs_started += 1 

        elif current_job.execution_time == current_job.remaining_exec_time:
            current_job.start_job(t)
            num_jobs_started += 1 
        else:
            current_job.resume_job()
        
        # do stuff
    return num_jobs_started, num_jobs_completed_in_time

def RM_Simulation(n, task_set):
    # Sort tasks with ascending order of periods
    task_set.sort(key=lambda task: task.Period)
    return Simulation(n, task_set)

def SPTF_Simulation(n, task_set):
    # Sort tasks with ascending order of execution times
    task_set.sort(key=lambda task: task.WCET)
    return Simulation(n, task_set)

def MUF_Simulation(n, task_set):
    # Sort tasks with descending order of utilization
    task_set.sort(key=lambda task: task.Utilization, reverse=True)
    return Simulation(n, task_set)

def simulation():

    # num_tasks_test_arr = [16]
    # num_tasks_test_arr = [8, 16, 32, 64]
    task_set_utilizations = [round(0.10 * i, 2) for i in range(1, 11)]

    num_task_sets = 1 # For Testing
    # num_time_units = 100000

    # num_task_sets = 100000

    num_tasks = 2
    print("Num Tasks: {}".format(num_tasks))

    fraction_RM_successful = [0 for i in range(1, 11)]
    fraction_SPTF_successful = [0 for i in range(1, 11)]
    fraction_MUF_successful = [0 for i in range(1, 11)]
    
    for j in range(len(task_set_utilizations)):

        utilization = task_set_utilizations[j]
        print("Utilization: {}\n".format(utilization))

        print("Generating Task Sets")
        scatter_arr = np.zeros(shape=(num_task_sets, num_tasks))
        print(num_task_sets, num_tasks)
        # Create a list of task sets for current number of tasks        
        task_sets = []
        for k in range(num_task_sets):
            scatter_arr[k] = getUniformVector(num_tasks)
            task_sets.append(getTaskSet(scatter_arr[k], utilization))


        # print("Start Testing Schedulability at current Utilization")
        num_successful_RM_completions = 0
        num_rm_started = 0

        num_successful_SPTF_completions = 0
        num_sptf_started = 0

        num_successful_MUF_completions = 0
        num_muf_started = 0

        for l in range(num_task_sets):
            started = 0
            completed = 0

            started, completed = RM_Simulation(num_tasks, task_sets[l])
            num_rm_started = started
            num_successful_RM_completions +=  completed

            started, completed = SPTF_Simulation(num_tasks, task_sets[l])
            num_sptf_started = started
            num_successful_SPTF_completions += completed

            started, completed = MUF_Simulation(num_tasks, task_sets[l])
            num_muf_started = started
            num_successful_MUF_completions +=  completed

               
        fraction_RM_successful[j] = float(num_successful_RM_completions) / float(num_rm_started)
        fraction_SPTF_successful[j] = float(num_successful_SPTF_completions) / float(num_sptf_started)
        fraction_MUF_successful[j] = float(num_successful_MUF_completions) / float(num_muf_started)

        print("Fraction RM Completed: {}".format(round(fraction_RM_successful[j], 2)))
        print("Fraction SPTF Completed: {}".format(round(fraction_SPTF_successful[j], 2)))
        print("Fraction MUF Completed: {}".format(round(fraction_MUF_successful[j], 2)))

        print("\n-------------------------------------------\n")

    # print("Saving figure for num tasks: {}".format(num_tasks))

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    ax.plot(task_set_utilizations, np.array(fraction_RM_successful) * 100, marker='.', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label="Fraction RM Completed")
    ax.plot(task_set_utilizations, np.array(fraction_SPTF_successful) * 100, marker='^',markerfacecolor='red', markersize=10, color='lightcoral', linewidth=4, label="Fraction SPTF Completed")
    ax.plot(task_set_utilizations, np.array(fraction_MUF_successful) * 100,marker='s', markerfacecolor='green', markersize=10, color='olive', linewidth=4, label="Fraction MUF Completed")
    ax.set_xlabel('Utilization')
    ax.set_ylabel('Percentage Jobs Completed before Deadline')
    plt.legend(loc="best")
    plt.savefig('figs/{}CompletionPercentage.png'.format(num_tasks))
        # plt.show()
        # ax = fig.add_subplot(111,projection='3d')
    print("\n")