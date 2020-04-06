import json , urllib.request
from collections import Counter
import itertools
from collections import MutableMapping 
from collections import defaultdict
import csv

def convert_flatten(d, parent_key ='', sep ='_'): 
    items = [] 
    for k, v in d.items(): 
        new_key = parent_key + sep + k if parent_key else k 
  
        if isinstance(v, MutableMapping): 
            items.extend(convert_flatten(v, new_key, sep = sep).items()) 
        else: 
            items.append((new_key, v)) 
    return dict(items) 

def get_all_values(nested_dictionary):
    count = 0
    for key, value in nested_dictionary.items():

        if type(value) is dict:

            get_all_values(value)

        else:

            print(key, ":", value)
            count = count + 1
            if count > 1:
                break

def GetRawData():
    with urllib.request.urlopen("https://api.covid19india.org/raw_data.json") as url:
     data = json.loads(url.read().decode())
     #data = cleanRawData(data)
    return(data)

def cleanRawData(data):
    data = GetRawData()
    len1 = len(data['raw_data'])
    for i in range(len(data['raw_data'])) :
        if (data['raw_data'][i]['detectedstate']) == "Delhi" :
             data['raw_data'][i]['detecteddistrict'] = "Delhi"
    return(data)

def GetDates():
    with urllib.request.urlopen("https://api.covid19india.org/raw_data.json") as url:
     data = json.loads(url.read().decode())
    Dates = extract_element_from_json(data,["raw_data","dateannounced"])
    return(unique(Dates))

def GetTopTrends(data):
    Hotspots = GetTop10Districts(data)
    cityTrends = defaultdict(list)
    cases = data.get('raw_data',{})
    for case in cases:
        for key in case.keys():
            if key == "detecteddistrict" and case[key] in Hotspots and case[key] != "" :
                cityTrends[case[key]].append(case.get("dateannounced"))
    return(cityTrends)

def GetStateTrends(data):
    cases = data.get('raw_data',{})
    stateTrends = defaultdict(list)
    for case in cases:
        for key in case.keys():
            if key == "detectedstate" and case[key] != "" :
                stateTrends[case[key]].append(case.get("dateannounced"))
    return(stateTrends)

def GetTop10Districts(data):
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
    return(Top10Final)



def GetTop10DistrictsWithNumbers(data):
    Districts = extract_element_from_json(data,["raw_data","detecteddistrict"])
    #print(type(Districts))
    District_wide_Count = Counter(Districts)
    #print(type(District_wide_Count))
    Top10counts = District_wide_Count.most_common()[:10]
    return(Top10counts)

def GetCSVfromList(mylist,csvname):
    with open(csvname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(mylist)

def GetCSVfromDict(mydict,csvname):
    with open(csvname, 'w') as f:
        for key in mydict.keys():
            f.write("%s,%s\n"%(key,mydict[key]))
        

def extract_element_from_json(obj, path):
    '''
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return(unique_list)