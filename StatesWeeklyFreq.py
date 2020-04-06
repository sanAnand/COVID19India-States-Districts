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

# Create nested dictionary in thr format: {Week Number: {{State 1: count}, {State 2: count}}}
Weeks = list(range(0,53))
WeeklyState = {}    
IndianStates = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Delhi","Puducherry"]
for week in Weeks:
    WeeklyState.update({'week' + str(week) :{'null': 0}})
for week in Weeks:
    for IndianState in IndianStates: 
        WeeklyState['week' + str(week)][IndianState] = 0
for week in Weeks:
    WeeklyState.update({week :{}})
    for a in aList: 
        WeeklyState['week'+str(a[1])][a[0]] = a[2]
        

# Export Weekly Frequency data to CSV 
with open("WeeklyStateDict.csv", 'w') as f:
        for key in WeeklyState.keys():
            f.write("%s,%s\n"%(key,WeeklyState[key]))




