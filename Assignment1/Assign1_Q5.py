#Wade Willms
#Assignment 1
#Money Game





penny = int(input("Enter amount of pennies: "))
nickel = int(input("Enter amount of nickels: "))
dime = int(input("Enter amount of dimes: "))
quarter = int(input("Enter amount of quarters: "))

dollar = (penny*.01 + nickel*.05 + dime*.1 + quarter*.25)

print("Total is: ", dollar)

if dollar == 1:
    print("This is a dollar")
elif dollar > 1:
    print("This is more than a dollar")
else:
    print("This is less than a dollar")
