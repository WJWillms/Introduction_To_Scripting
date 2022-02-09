#Wade Willms
#Assignment 2
#Question 4
#Sorting list, new list, math in list



list = [20, 68, 41, 88, 16, 40, 65, 97, 85]

counter = 0

total = 0 #holds the sum of list
while counter < len(list):
    total = total + list[counter]
    counter +=1

print(list)
print("The list sum:", total)

listTwo = [2,4,6,8,10]
listThree = [1,3,5,7,9]


counter = 0

totalTwo = 0 #holds the sum of list
while counter < len(listTwo):
    totalTwo = totalTwo + listTwo[counter]
    counter +=1
    
counter = 0

totalThree = 0 #holds the sum of list
while counter < len(listThree):
    totalThree = totalThree + listThree[counter]
    counter +=1
    
    
print(listTwo)
print(totalTwo)
print(listThree)
print(totalThree)