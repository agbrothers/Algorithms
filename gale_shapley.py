import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

pop = 6

# Define the Data Structures
men = np.zeros((pop, pop+1), dtype = 'int32')
women = np.zeros((pop, pop+1), dtype = 'int32')
for k in range(pop):
    men[k,1:] = rd.sample(range(pop), pop)
    women[k,1:] = rd.sample(range(pop), pop)
men[:,0] = pop
women[:,0] = pop

# Assign Matchings
i = 0
while np.all(men[:,0] != pop) == False:
    if men[i,0] == pop:
        for j in range(1,pop+1):
            current = men[i,j]
            if women[current,0] == pop:
                men[i,0] = current   # show the ith man is matched
                women[current,0] = i   # pair the women with the ith man
                break
                
    # else if the new man is on the woman's list, check to see if it comes before the already paired men
    else:
        for k in range(1,pop):
            if women[current,k] == women[current,0]:
                break
            elif women[current,k] == i:
                men[women[current,0],0] = pop
                men[i,0] = current
                women[current,0] = i
                break
        break
    i+=1

print('Each row represents a man/woman, and the first column represents the index of the man/woman they\'re matched to. The rest of the columns make up the preference list of each individual. \n' )
print('Men\'s Preference List \n', men)    
print('\nWomen\'s Preference List \n', women)    
