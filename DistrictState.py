import json 
from external import extract_element_from_json, unique
from collections import Counter
# some JSON:
with open('raw_data.json') as json_file:
    y = json.load(json_file)
DS = extract_element_from_json(y,["raw_data","detectedstate"])
print(Counter(DS))
