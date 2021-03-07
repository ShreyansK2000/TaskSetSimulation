from random import *
import numpy as np

def getNRandom(n=10):
    rands = []
    for i in range(n):
        rands.append(np.random.uniform(0,1,None))

    return rands

def getUniformVector(num_tasks):
    rands = getNRandom(num_tasks)
    # n = num_tasks

    # y_i = -log(x_i)
    randys = -1. * np.log(np.array(rands))

    # sum_randys = (y_1 + y_2 + .. y_n)
    sum_randys = np.sum(randys)
    # print("Rand ys: ", randys)
    # print("Sum Rand ys", sum_randys)

    
    # print(randys)
    # rands.sort()
    # ret = []
    # for i in range(n):
    #     if i == 0:
    #         ret.append(rands[i] - 0.)
    #     elif i == n - 1:
    #         ret.append(1. - rands[i-1])
    #     else: 
    #         ret.append(rands[i] - rands[i-1])
    # (y1, y2, ... yn) / (y_1 + y_2 + .. y_n)
    
    return np.true_divide(randys, sum_randys)
