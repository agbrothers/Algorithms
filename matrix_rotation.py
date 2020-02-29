import numpy as np
import pandas as pd
import random


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
rot = 90

def rotateCCW(arr, angle):
    
    # rotate 90 degrees counter-clockwise until angle/90 iterations occur
    k=0
    while k < angle/90:
        x = []
        for i in arr:
            x.append(list(i[::-1]))
        arr = np.array(list(zip(*x)))
        k+=1
    return(arr)

def rotateCW(arr, angle):
    
    # rotate 90 degrees clockwise until angle/90 iterations occur
    k=0
    while k < angle/90:
        arr = np.array(list(zip(*arr)))
        x = []
        for i in arr:
            x.append(list(i[::-1]))
        k+=1
    return(np.array(x))


angles = [90,180,270,360]
angle = random.choice(angles)
n = random.randint(1,10)
M = np.random.randint(1,100, size=(n,n))
print(M, '\n')
print(rotateCW(M, angle))
print(angle)


# time complexity O(nm), n = dim matrix, m = number of rotations