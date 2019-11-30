import json
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process

data = json.load(open("D:\Courses\Practice\data.json"))

def translate(w):
    w = w.lower()
    match_case = process.extractOne(w, data.keys())
    print(match_case)
    if match_case:
        if match_case[1] == 100:
            return data[w]
        else:
           yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % str(process.extract(w, data.keys())[0][0]))
           yn = yn.upper()
           if yn == "Y":
               return data[str(process.extract(w, data.keys())[0][0])]
           elif yn == "N":
               return "The word doesn't exist. Please double check it."
           else:
               return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
#print(type(process.extractOne(word.lower(), data.keys())))
