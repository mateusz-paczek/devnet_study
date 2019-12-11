#!/usr/bin/python3

#Modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

#Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. 
#If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

import json

#define birthday dictionary
birthday = {}

#load birthday.json file content into this dictionary
with open("birthday.json") as f:
	birthday = json.load(f)

#Creating function to add entry in dictionary and then update JSON file from disk
def add_entry():
	name = input(f"Who do you want to add to Birthday Dictionary \n").title()
	date = input(f"When is {name} born ?\n")
	
	#creating dictionary element
	birthday[name] = date
	
	#Adding this entry to birthday.json file
	with open("birthday.json", "w") as f:
		json.dump(birthday,f)
	print (f"{name} was added to the birthday list \n")


#Finding date of birthday of specific person
def find_date():
	name = input("Whose name you would like to check ? \n")
	try:
		if birthday[name]:
			print(f"{name} has his birthday on {birthday[name]} \n")
	except KeyError:
		print(f"{name} is not in the list")


#listing all entries in Birthday dictionary
def list_entries():
	print("The current entries in my birthday list are: \n++++++++++++++++++++++++++++++++++++++++++++++")
	for name in birthday:
		print (name.ljust(31), ":", birthday[name])

#Defining user options:
while True:
	what_next = input("What do you want to do: Add, Find, List, Quit\n").capitalize()
	if what_next == "Quit":
		print("GoodBye")
		raise SystemExit(0)
	elif what_next == "Add":
		add_entry()
	elif what_next == "Find":
		find_date()
	elif what_next == "List":
		list_entries()
	else:
		print("Please specify correct action\n")

