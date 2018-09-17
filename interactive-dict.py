# word = key to be entered
# data = dictionary from json file

import json
from difflib import get_close_matches
data_dict = json.load(open("data.json"))
word = input("Enter word for definition: ")

def word_def(word,dictionary):
	word = word.lower()
	if word in dictionary:
		defi = dictionary[word]
		return defi
	elif word.title() in dictionary:
		defi = dictionary[word.title()]
		return defi
	elif word.upper() in dictionary:
		defi = dictionary[word.upper()]
		return defi
	elif len(get_close_matches(word,dictionary.keys()))>0:
		yn = input("Did you mean %s instead? y/n: " % get_close_matches(word,dictionary.keys())[0])
		if yn == "y":
			return dictionary[get_close_matches(word,dictionary.keys())[0]]
		elif yn == "n":
			return "The word doesn't exist. Please double check it."
		else:
			return "We didn't understand your entry."
	else:
		return "The word does not exist"
	
output = word_def(word,data_dict)

if type(output) == list:
	for itm in output:
		print(itm)
else:
	print(output)
