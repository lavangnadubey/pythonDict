import json
#library to match text
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


#print(SequenceMatcher(None,"rain","rainnn").ratio())
def translate(word):
    try:
        return data[word]
    except KeyError:
        if (get_close_matches(word, data.keys()))==[]:
            return "No such word found !! Please double check"
        else:
            print("Did you meant "+get_close_matches(word, data.keys())[0]+" ?")
            ch=input('Enter Y/N:')
            if (ch=='y'or ch=='Y'):

                return translate(get_close_matches(word, data.keys())[0])
            else:
                return 'Sorry !! Check again '



data = json.load(open("data.json"))
user_choice = input("Enter word :")
if user_choice.isupper() or user_choice[0].isupper():
    output=(translate(user_choice))
else:
    output=(translate(user_choice.lower()))
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)