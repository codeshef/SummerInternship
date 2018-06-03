
# Creating dictionary in python


import json

from difflib import get_close_matches

data = json.load(open("data.json"))


def dictSearching(w):

    print("Searching word ......")

    w = w.lower()

    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys()) )> 0:

        choice= input("Did You mean %s instead ? If yes press Y else No")

        if choice == "Y":
            return  data[get_close_matches(w, data.keys())[0]]

        elif choice == "N":
            return "The word doesn't exist !! Please Check again"
        else:
            return "Dictionary is not able to recognize that word!!!"


word = input("Enter word to search in dictionary : ")

output = dictSearching(word)

print(output)
