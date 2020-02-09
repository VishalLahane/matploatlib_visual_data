# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:13:31 2020

@author: vlahane
"""

from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('countries.csv')
print(df.head()) # gives 1st five rows
print(df.country) # select only country column
only_Afghanistan_col=df.country == 'Afghanistan' # gives row wise true or false
only_Afghanistan_data= df[df.country == 'Afghanistan']
plt.plot(only_Afghanistan_data.year,only_Afghanistan_data.gdpPerCapita)
plt.title("Afghanistan's GDP Per Capita")
#plt.show()
plt.savefig('exported_imgage3')
plt.show()  