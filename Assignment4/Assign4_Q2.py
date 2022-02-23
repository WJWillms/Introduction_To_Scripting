#Wade Willms
#Assignment 4
#Question 2
#List append
numbers = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ While loop for user input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
i=0
while i < 20:
	value = (int(input("Enter a Number: ")))
	numbers.append(value)
	i += 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~ While loop for user input end ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
 
print("The Lowest: " + str(min(numbers))) 
print("The Highest: " + str(max(numbers))) 
print("The Sum: " + str(sum(numbers))) 
print("The Average: " + str(sum(numbers)/len(numbers))) 