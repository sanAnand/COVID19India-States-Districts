import json , urllib.request
from external import extract_element_from_json, unique, GetTop10Districts, GetDates, GetRawData, get_all_values, convert_flatten, cleanRawData , GetTop10DistrictsWithNumbers, GetCSVfromDict, GetCSVfromList, GetTopTrends
from collections import Counter
import itertools
from functools import reduce
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import sys
from datetime import datetime

b = np.array([[1,2,3],[4,5,6]]) 
print(b)
np.savetxt('numpytest.csv', [b],delimiter=",", fmt="%d")

'''
#d = np.array([['city','week','frequency']])
d = np.array([])
print(d)
print('*****')

rawData = GetRawData()
cityTrends = GetTopTrends(rawData)
master = {}
cnt = Counter()
for city in cityTrends :
    cnt = Counter(cityTrends[city])
    master[city] = dict(cnt)
#print((master['Bengaluru']))
for i in master.keys() : 
    for key,value in master[i].items() :
        a_date = datetime.strptime(key,'%d/%m/%Y')
        week_number = a_date.isocalendar()[1]
        d = np.append(d,[[i,week_number,value]])
#print(d)
np.savetxt('data.csv', [d],delimiter=",", fmt="%s")
'''