#Wade Willms
#Assignment 2
#Question 8
#Fibonacci sequence

def Fibonacci(num):
 
    # if 0 returns 0
    if num == 0:
        return 0
 
    # If 1 or 2 returns 1
    elif num == 1 or num == 2:
        return 1
 
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)
        
        
x =int(input("Enter a number for the Fibonacci Sequence: "))
if x >=1:
    print(Fibonacci(x))
elif x < 0:
    print("Number must be greater than 0")
    