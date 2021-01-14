import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def thesaurus(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        yn = input("Did you mean %s instead. If so, please enter Y else N: " % get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            print("Great! Here you go!")
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        else:
            return "Sorry! Please try again"
    else:
        return "No such word"

w = input("Enter the word: ")
output = thesaurus(w)

if type(output)==list:
    for a in output:
        print(a)
else:
    print(output)