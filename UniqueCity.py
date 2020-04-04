import json , urllib.request
from external import extract_element_from_json, unique
from collections import Counter
import itertools
with urllib.request.urlopen("https://api.covid19india.org/raw_data.json") as url:
    data = json.loads(url.read().decode())
Districts = extract_element_from_json(data,["raw_data","detecteddistrict"])
District_wide_Count = Counter(Districts)
Top10counts = District_wide_Count.most_common()[:11]
Top10districts = []
for district in Top10counts :
    Top10districts.append((str(district).split(",")[0]))  
Top10Final=[]
for i in Top10districts:
    j=i.replace("'","")
    Top10Final.append(str(j.split("(")[1]))
print(Top10Final)




'''
with open('raw_data.json') as json_file:
 y = json.load(json_file)
Districts = extract_element_from_json(y,["raw_data","detecteddistrict"])
District_wide_Count = Counter(Districts)
Top10counts = District_wide_Count.most_common()[:11]
Top10districts = []
for district in Top10counts :
    Top10districts.append((str(district).split(",")[0]))  
Top10Final=[]
for i in Top10districts:
    j=i.replace("'","")
    Top10Final.append(str(j.split("(")[1]))
print(Top10Final)
'''

