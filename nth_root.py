import numpy as np
import pandas as pd
import random

# what the fuck is the nth root
# i * i * ...n times... * i = input

# how do I do sqrt

def squareRoot(x):    
    #i*i = x   # think of this as a hypotenuse    
    k1 = 0
    while k1*k1 < x:
        k1+=1
    k0 = k1-1    
    return(x)



def nRoot(x, n):
    tol = 10e-10
    a,b = 0,x
    k=0
    
    # root bracketing approach
    while np.abs(pow((b+a)/2,n)-x) > tol and k < 200:
        mid = np.abs((b+a)/2)
        if pow(mid,n) > x:
            b = mid
            
        elif pow(mid,n) < x:
            a = mid
            
        else:
            return(mid)
        k+=1

    return(round((b+a)/2,9))
