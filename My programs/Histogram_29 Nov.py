#!/usr/bin/env python
# coding: utf-8

# In[69]:


import random as rd
import statistics as st
from matplotlib import pyplot as plt


# In[111]:


#Initialising the lists for mean and median so that they are empty everytime the code runs
medianlist = []
meanlist = []

#using a for loop to generate 10,0000 random samples
for i in range(100000):
    # using the randrange function to generate a random number from 1 to 100 and then 
    # organising it into a list of 10 random numbers
    res = [rd.randrange(1, 100) for i in range(10)]
    #finding the median of the numbers
    mdn = st.median(res)
    #generating a list of all the medians so that it can be plotted later
    medianlist.append(mdn)
    #finding the mean of the numbers
    mn = st.mean(res)
    #generating a list of all the means so that it can be plotted later
    meanlist.append(mn)
    
#print(medianlist)
#print(meanlist)

#plotting the histogram for mean
fig, ax = plt.subplots()
ax.set_title("Histogram for all the means")
ax.hist(meanlist, edgecolor="black", color="pink", bins = 100)

#plotting the histogram for median
fig, ax = plt.subplots()
ax.set_title("Histogram for all the medians")
ax.hist(medianlist, edgecolor="black", color="lightblue", bins = 100)


# In[109]:


get_ipython().run_line_magic('pinfo', 'ax.hist')


# In[ ]:




