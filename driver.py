from plot3d import *
from random_vector_generator import *
from task_set import *
import matplotlib.pyplot as plt
import math
from rta import *
from simulation import *

def rta_driver():

    # num_tasks_test_arr = [3]
    num_tasks_test_arr = [8, 16, 32, 64]
    task_set_utilizations = [round(0.05 * i, 2) for i in range(1, 21)]

    
    # num_task_sets = 10 # For Testing
    num_task_sets = 100000
    for i in range(len(num_tasks_test_arr)):

        num_tasks = num_tasks_test_arr[i]
        fraction_RM_schedulable = [0 for i in range(1, 21)]
        fraction_SPTF_schedulable = [0 for i in range(1, 21)]
        fraction_MUF_schedulable = [0 for i in range(1, 21)]
        
        for j in range(len(task_set_utilizations)):

            utilization = task_set_utilizations[j]
            print("Num Tasks: {}".format(num_tasks))
            print("Utilization: {}\n".format(utilization))


            print("Generating Task Sets")
            scatter_arr = np.zeros(shape=(num_task_sets, num_tasks))

            # Create a list of task sets for current number of tasks        
            task_sets = []
            for k in range(num_task_sets):
                scatter_arr[k] = getUniformVector(num_tasks)
                task_sets.append(getTaskSet(scatter_arr[k], utilization))
 

            # print("Task set utilization: {}\n\n".format(round(sum(task.Utilization for task in task_sets[0]), 2)))
            # print("\n\n")

            print("Start Testing Schedulability at current Utilization")
            num_RM_Schedulable = 0
            num_SPTF_Schedulable = 0
            num_MUF_Schedulable = 0
            for l in range(num_task_sets):
                num_RM_Schedulable += RM_RTA_Schedulable(task_sets[l])
                num_SPTF_Schedulable += SPTF_RTA_Schedulable(task_sets[l])
                num_MUF_Schedulable += MUF_RTA_Schedulable(task_sets[l])

        
            fraction_RM_schedulable[j] = float(num_RM_Schedulable) / float(num_task_sets)
            fraction_SPTF_schedulable[j] = float(num_SPTF_Schedulable) / float(num_task_sets)
            fraction_MUF_schedulable[j] = float(num_MUF_Schedulable) / float(num_task_sets)

            print("Fraction RM Schedulable: {}".format(round(fraction_RM_schedulable[j], 2)))
            print("Fraction SPTF Schedulable: {}".format(round(fraction_SPTF_schedulable[j], 2)))
            print("Fraction MUF Schedulable: {}".format(round(fraction_MUF_schedulable[j], 2)))

            print("\n-------------------------------------------\n")

        print("Saving figure for num tasks: {}".format(num_tasks))

        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111)
        ax.plot(task_set_utilizations, fraction_RM_schedulable, marker='.', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label="Fraction RM Schedulable")
        ax.plot(task_set_utilizations, fraction_SPTF_schedulable, marker='^',markerfacecolor='red', markersize=10, color='lightcoral', linewidth=4, label="Fraction SPTF Schedulable")
        ax.plot(task_set_utilizations, fraction_MUF_schedulable,marker='s', markerfacecolor='green', markersize=10, color='olive', linewidth=4, label="Fraction MUF Schedulable")
        ax.set_xlabel('Utilization')
        ax.set_ylabel('Fraction Schedulable Task')
        plt.legend(loc="best")
        plt.savefig('figs/{}TasksSchedulability.png'.format(num_tasks))
        # plt.show()
        # ax = fig.add_subplot(111,projection='3d')
        print("\n")
    # # Plotting simplex stuff
    # fig = plt.figure(figsize=(8, 8))
    # # Add an axes
    # ax = fig.add_subplot(111,projection='3d')
    # # ax.set_proj_type('ortho')
    # ax.view_init(30, 45) 
    # ax = plotSimplex(ax)
    # # ax.set_aspect(1 / ax.get_data_ratio())
    # ax.scatter(scatter_arr[:,0], scatter_arr[:,1], scatter_arr[:,2], marker="o", s=2, depthshade=False)


    # plt.show()

if __name__ == '__main__':
    # Comment or uncomment to run RTA for the three policies
    # rta_driver()

    # Comment of uncomment to run Simulation for the three policies
    simulation()