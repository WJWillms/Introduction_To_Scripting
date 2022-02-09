#Wade Willms
#Assignment 2
#Question 3
#Sorting Loop


list = [20, 68, 41, 88, 16, 40, 65, 97, 85]

print("List before Sort")
print(list)

counter = 0
while counter < len(list):
    counterTwo = counter + 1
    while counterTwo < len(list):
        if list[counter] > list[counterTwo]:
            temp = list[counter]
            list[counter] = list[counterTwo]
            list[counterTwo] = temp
        counterTwo = counterTwo + 1
    counter = counter + 1


print("List afer sort")
print(list)
