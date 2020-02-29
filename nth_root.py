import numpy as np


""" Coding Challenge, write a function that returns a number's nth root """

def nRoot(x, n):
    tol = 10e-10
    a,b = 0,x
    k=0
    
    # simple root bracketing approach
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
