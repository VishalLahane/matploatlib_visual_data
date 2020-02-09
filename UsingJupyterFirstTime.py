#!/usr/bin/env python
# coding: utf-8

# In[ ]:





from matplotlib import pyplot as plt

# In[22]:

plt.plot([1,2,3],[1,4,9])
plt.plot([1,2,3],[10,20,30])
plt.xlabel("this is x axis")
plt.ylabel("this is y axis")
plt.title("plot title")
plt.legend(["Dataset 1","Dataset 2"])

#plt.legend() takes a list as an agrumnet

plt.savefig('exported_imgage1')
plt.show() # shows plot 

# In[ ]:




