import numpy as np
import time
import matplotlib.pyplot as plt


# Implementing the Merge Sort Algorithm and Comparing it to brute force methods

# define the array of integers we want sorted
x = [1,43,24,5,6,24,8,69,0,5,35,5,7,3,42,9,46,8,7,35,65,-3]
y = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

def brute_force(x):
    start = time.time()
    i = 0
    sort = False
    while sort == False and i < 30:
        if i < len(x)-1 and x[i] > x[i+1]:
            a = x[i]
            x[i] = x[i+1]
            x[i+1] = a
            i = 0
        else:
            i+=1
        if i > len(x):
            sort = True
    end = time.time()
    print(end-start)
    return(x)



# Combine two lists sorting elements from smallest to largest 
def merge(a,b):
    n = len(a)
    m = len(b)
    c = np.zeros(n+m, dtype = 'int')
    i=j=k=0
    while i < n or j < m:
        if j >= m or i < n and a[i] < b[j]:
            c[k] = a[i]
            i+=1
        else:
            c[k] = b[j]
            j+=1
        k+=1
    return(list(c))
      
    
# Sort any list via Divide and Conquer style recursion
# Note the first time printed is the total runtime
def merge_sort(x):
    start = time.time()
    mid = int(np.floor(len(x)/2))
    a = x[:mid]
    b = x[mid:]
    if len(x) == 2:
        return(merge(a,b))
    elif len(x) == 3:
        return(merge(a,merge_sort(b)))
    else:
        end = time.time()
        print(end-start)
        return(merge(merge_sort(a),merge_sort(b)))