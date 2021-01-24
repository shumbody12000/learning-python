######
#Learning Python
#David
###########

#clear the terminal screen
import os
os .system('clear')

#######################
#DATA TYPES
#Strings
#Numbers
#Lists
#Tuples
#Dictionaries
#Boolean
#######################

num = 1
fizzcount = 0
buzzcount = 0
fizzbuzzcount = 0

while (num <= 100):
	if(num % 3 == 0) and (num % 5 == 0):
		print (str(num) + ". fizzbuzz")
		fizzbuzzcount += 1

	elif (num % 3 == 0):
		print(str(num) + ". fizz")
		fizzcount += 1
	
	elif (num % 5 == 0):
		print(str(num) + ". buzz")
		buzzcount += 1
	else:
		print(num)
	num +=1	

print ("__________________________")
print ("fizz\tbuzz\tfizzbuzz")
print (str(fizzcount) + "\t" + str(buzzcount) + "\t" + str(fizzbuzzcount))