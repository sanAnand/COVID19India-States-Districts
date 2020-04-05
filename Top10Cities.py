import json , urllib.request, operator
from external import extract_element_from_json, unique, GetTop10Districts, GetDates, GetRawData, cleanRawData , GetTopTrends , GetCSVfromDict
from collections import Counter
import itertools
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

rawData = GetRawData() # Make API call to get raw case data
rawData = cleanRawData(rawData) # Clean data to fix Delhi issue
cases = rawData.get('raw_data',{}) # Get info about all cases
cityTrends = GetTopTrends(rawData) # Get info about top 10 cities. City and dates with cases (no frequency)
CityTrendsDailyFreq = {} # initialize a dictionary to hold daily frequency data
cnt = Counter() # initalize counter to calculate daily frequency data
d = np.array([]) # initialize numpy array to hold weekly data ('city', week number, # of cases)

# Loop through CityTrends and generate daily count 
for city in cityTrends :
    cnt = Counter(cityTrends[city])
    CityTrendsDailyFreq[city] = dict(cnt)
#print(CityTrendsDailyFreq)
# Loop through daily count and generate weekly count -- not perfect. In some cases, there will multiple entries for each week. Need to add when we generate report 
aList = []
for i in CityTrendsDailyFreq.keys() : 
    for key,value in CityTrendsDailyFreq[i].items() :
        a_date = datetime.strptime(key,'%d/%m/%Y')
        week_number = a_date.isocalendar()[1]
        #d = np.append(d,[[i,week_number,value]])
        #d = np.append(d,list([i,week_number,value]))
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

#print("****")
print(aList)
#print(d)
# Export Weekly Frequency data to CSV 
np.savetxt('HotSpotWeeklyFreq.csv', aList,delimiter=",", fmt="%s", header="City, Week,Frequency")

