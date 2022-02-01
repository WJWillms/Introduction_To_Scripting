#Wade Willms
#Assignment 1
#Question 5
#Money Game





penny = int(input("Enter amount of pennies: "))
nickel = int(input("Enter amount of nickels: "))
dime = int(input("Enter amount of dimes: "))
quarter = int(input("Enter amount of quarters: "))

#Take all inputs and multiple by change amount to get to total
dollar = (penny*.01 + nickel*.05 + dime*.1 + quarter*.25)

print("Total is: ", dollar)

#Else if to dtermine more less than dollar output.
if dollar == 1:
    print("This is a dollar")
elif dollar > 1:
    print("This is more than a dollar")
else:
    print("This is less than a dollar")
