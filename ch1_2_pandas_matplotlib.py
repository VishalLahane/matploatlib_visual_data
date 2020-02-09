# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:08:30 2020

@author: vlahane
"""

from matplotlib import pyplot as plt
import pandas as pd

data = { 
        'year': [2008,2012,2016],
        'attendees':[112,321,729],
        'average age': [24,23,31]
        }
df = pd.DataFrame(data)
print(df)
print("**************************************")
print(df['year'])

earlier_than_2013=df['year'] < 2013

""" boolean indexing """
print(df[earlier_than_2013]) 

plt.plot(df['year'], df['attendees'])
plt.plot(df['year'], df['average age'])
plt.legend(["attendees","average age"])
plt.show()
plt.savefig('exported_imgage2')

