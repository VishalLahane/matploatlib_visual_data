# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:39:12 2020

@author: vlahane
"""

from matplotlib import pyplot as plot
import pandas as pd

data = pd.read_csv('countries.csv')

data_1997 = data[data.year == 1997]
europe_1997 = data_1997[data_1997.continent=='Europe']
# europe_1997.head
americas_1997 = data_1997[data_1997.continent=='Americas']
# americas_1997.head
plot.subplot(2 , 1, 1)
plot.title('Distribution of life expectancy')
plot.ylabel('Europe')
buckets = 15
plot.hist(europe_1997.lifeExpectancy, buckets, edgeColor='black', range=(60, 100))
plot.subplot(2, 1, 2)
plot.ylabel('Americas')
plot.hist(americas_1997.lifeExpectancy, buckets, edgeColor='black', range=(60, 100))
plot.savefig('life-expectancy-dist-europe-americas-1997')
print(americas_1997[americas_1997.lifeExpectancy<65])
plot.show()