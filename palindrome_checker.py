#!/usr/bin/python3

#Ask the user for a string and print out whether the string is palindrome or not. (A palindrome is a string that reads the same forwards and backwards)

word = input("Please write your string: ")
#Make a given string a string 
word = str(word)
#define rvs variable - word variable backwards
rvs=word[::-1]
print(rvs)

#comparing word and rvs variable
if word == rvs:
	print("This word is a palindrome")
else:
	print("This word is not a palindrome")

