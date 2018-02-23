
# coding: utf-8

# In[1]:


import os 
import math
import numpy as np


# In[151]:


def ramanujan(c):
    ram = np.zeros(shape=(c,c), dtype=np.uint32)
    i=0   
    while (i<c):
        j=0
        while(j<c):
            ram[i][j] = (i+1)**3 + (j+1)**3
            j = j+1
        i = i+1
    
    # This block is to easily find these special numbers without knowing their factors.
    #But, as we are also interested in the factors, wrote a different method below.
    """unique, unique_counts = np.unique(ram, return_counts = True)
    length = len(unique_counts)
    i=0
    output = []
    while i<length:
        if unique_counts[i] == 4:
            output.append(unique[i]) 
        i = i+1"""
    
    output =[]
    for i in range (0,c):
        for j in range (0,c):
            s=0
            for x in range (0,c):
                for y in range (0,c):
                    if ram[x][y] == ram[i][j]:
                        s = s+1                       
            if s==4:
                output.append([ram[i][j], i+1, j+1])             
   
    # This loop just to eliminate the duplicates. Blocking this loop and returning the output will still give you solution,
    # but with repetitions.    
    for i in range (0, len(output)):
        for j in range(0, len(output)):
            if i != j and output[j][0] == output[i][0] and output[j][1] == output[i][2]:                
                output[j] = output[i]         
                
    output_unique = np.unique(output, axis=0)       
    return output_unique[np.lexsort(np.fliplr(output_unique).T)]


# In[154]:


ramanujan(25)

