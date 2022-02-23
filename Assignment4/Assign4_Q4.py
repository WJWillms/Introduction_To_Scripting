#Wade Willms
#Assignment 4
#Question 3
#2nd largest/random list
import random

#~~~~~~~~~~~~~~~~~~~~~ Part 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~
numbers = []
for i in range(100):
	num = random.randint(0,20)
	numbers.append(num)
print("Part 1 list:")
print(numbers)
#~~~~~~~~~~~~~~~~~~~~~ Part 1 End ~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~Part 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Nested while loop allows us to compare the current number to the current+1 number to see if they are the same
i=0
while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            del numbers[j]
        else:
            j += 1       
    i+=1       
print("Part 3 List:")
print(numbers)
#~~~~~~~~~~~~~~~~~~~~~~Part 3 end ~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~Part 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Numbers set lower than list numbers in case 20 appeared first in list causing 2nd highest to default to 20
first = -1
second = -1
k=0
#Find Highest
while k < len(numbers):
	if numbers[k] > first:
		first = numbers[k]
	k += 1
k=0
#Find 2nd Highest
while k < len(numbers):
	if numbers[k] > second and numbers[k] != first:
		second = numbers[k]	
	k += 1		
print("2nd Highest Number: " + str(second))
#~~~~~~~~~~~~~~~~~~~~~~Part 2 end ~~~~~~~~~~~~~~~~~~~~~~~


















