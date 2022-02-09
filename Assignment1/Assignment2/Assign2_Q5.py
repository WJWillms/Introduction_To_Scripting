#Wade Willms
#Assignment 2
#Question 5
#Finding prime numbers

#For loop cycles from numbers in range
for Number in range (2, 50):
    count = 0
    for i in range(2, (Number//2 + 1)):  #This for loop cycles through all numbers on the number that count is on to determine primeness
        if(Number % i == 0): #if the modulus doesn't equal 0 it is therfore not prime and the number in the range goes up one to evaluate
            count = count + 1
            break

    if (count == 0 and Number != 1): #If it goes through the for loop without increasing the count and the number in range isnt 1 it will print it as a prime number
        print(Number, end = '  ') #end = ' ' gives a space but keeps the outputs on the same line