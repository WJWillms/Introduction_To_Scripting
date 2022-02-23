#Wade Willms
#Assignment 4
#Question 3
#Dictionary


input=int(input("Input number: "))
book = dict()

#~~~~~~~~~~~~~~~~~ For loop for number to number+1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for x in range(1,input+1):
    book[x]=x*x
#~~~~~~~~~~~~~~~~~ For loop for number to number+1 end ~~~~~~~~~~~~~~~~~~~~~~~~~
print(book)