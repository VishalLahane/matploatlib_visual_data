# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 22:31:29 2020

@author: vlahane
"""

from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('countries.csv')

us = data[data.country =='United States']
us.head();
plt.plot(us.year,us.gdpPerCapita)
plt.xlabel("GDP per capita")
plt.ylabel("year")
plt.title("GDP compare")

china = data[data.country =='China']
plt.plot(china.year,china.gdpPerCapita)
plt.legend(['us','china'])
plt.show()