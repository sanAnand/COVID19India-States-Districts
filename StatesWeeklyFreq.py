import json , urllib.request
from external import extract_element_from_json, unique, GetTop10Districts, GetDates, GetRawData, get_all_values, convert_flatten, cleanRawData , GetTop10DistrictsWithNumbers, GetCSVfromDict, GetCSVfromList, GetTopTrends, GetStateTrends
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
np.set_printoptions(threshold=sys.maxsize)

data = GetRawData()
data = cleanRawData(data)
stateTrends = GetStateTrends(data)
#print(stateTrends)
stateTrendsDailyFreq = {} # initialize a dictionary to hold daily frequency data
cnt = Counter() # initalize counter to calculate daily frequency data
d = np.array([]) # initialize numpy array to hold weekly data ('state', week number, # of cases)


# Loop through State and generate daily count 
for state in stateTrends :
    cnt = Counter(stateTrends[state])
    stateTrendsDailyFreq[state] = dict(cnt)
#print(stateTrendsDailyFreq)

# Loop through daily count and generate weekly count -- not perfect. In some cases, there will multiple entries for each week. Need to add when we generate report 
aList=[]
for i in stateTrendsDailyFreq.keys() : 
    for key,value in stateTrendsDailyFreq[i].items() :
        a_date = datetime.strptime(key,'%d/%m/%Y')
        week_number = a_date.isocalendar()[1]
        #d = np.append(d,[[i,int(week_number),int(value)]])
        aList.append([i,int(week_number),int(value)])

for current, nex in zip(aList, aList[1:]): 
    if nex[0] == current[0] :
        #print(current[0], next[0])
        #print("in")  
        if nex[1] == current[1]:
            nex[2] = nex[2] + current[2]
            current[0] = '0'
            current[1] = 0
            current[2] = 0

#print(aList)



# Export Weekly Frequency data to CSV 
np.savetxt('StatesWeeklyFreq.csv', aList,delimiter=",", fmt="%s")

