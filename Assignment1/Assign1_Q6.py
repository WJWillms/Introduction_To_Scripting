#Wade Willms
#Assignment 1
#Question 6
#Leap Year Calculator

year = int(input("Enter a year: "))


#Modulus of 4 to determine leap year.
if year%4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
