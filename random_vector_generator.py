from random import *
import numpy as np

def getNRandom(n=10):
    rands = []
    for i in range(n-1):
        rands.append(np.random.uniform(0,1,None))

    return rands

def getUniformVector(num_tasks):
    rands = getNRandom(num_tasks)
    n = num_tasks
    rands.sort()
    ret = []
    for i in range(n):
        if i == 0:
            ret.append(rands[i] - 0.)
        elif i == n - 1:
            ret.append(1. - rands[i-1])
        else: 
            ret.append(rands[i] - rands[i-1])

    return ret
