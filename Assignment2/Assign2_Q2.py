#Wade Willms
#Assignment 2
#Question 2
#Factorial Math


numOne = int(input("Enter number 1: ")) #n
numTwo = int(input("Enter number 2: ")) #r

counter = 1 #counter

#three ints to hold the factorials calculated
factOne = 1
factTwo = 1
factThree = 1



while counter <= numOne:
    factOne = factOne * counter
    counter += 1
 
counter = 1 
    
    
while counter < numTwo:
    factTwo = factTwo * counter
    counter += 1
    
    
counter = 1

factThreeHelp = numOne - numTwo #calculates n-r for formula

while counter <= factThreeHelp:
    factThree = factThree * counter
    counter += 1
    
    
total = ((factOne)/(factTwo * factThree))

print("Total:",total)