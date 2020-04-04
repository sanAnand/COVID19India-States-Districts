import json , urllib.request, operator
from external import extract_element_from_json, unique, GetTop10Districts, GetDates, GetRawData, cleanRawData , GetTopTrends , GetCSVfromDict, GetTop10DistrictsWithNumbers, GetCSVfromList
from collections import Counter
import itertools
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


rawData = GetRawData() # Make API call to get raw case data
rawData = cleanRawData(rawData) # Clean data to fix Delhi issue
Top10Data = GetTop10DistrictsWithNumbers(rawData)
print(type(Top10Data))
GetCSVfromList(Top10Data,"Hotspots.csv")