# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

#!/usr/bin/python3

#define number 
number = int(input ("Please give your number to divide: "))

#define divisors list
divisors=[]

for num in range (1, number + 1):
	if number%num == 0:
		divisors.append(num)
print (divisors)
