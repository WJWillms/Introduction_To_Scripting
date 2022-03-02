#Wade Willms
#Assignment 5
#Question 5
#String Manipulation


def capbar(x):
    i = 0
    y = ""
    z=""
    while i < len(x):
        if i == 0:
            z = x[i].capitalize()
            y = y + str(z)
        elif x[i-1] == " ":
            z = x[i].capitalize()
            y = y + str(z)
        else:
            y = y + x[i]
        i += 1
    return y

def spacebar(x):
    i = 0
    y = ""
    while i < len(x):
        if x[i] == " ": 
            i += 1
        else:
            y = y + x[i]
            i += 1
    return y

def moneybar(x):
    i = 0
    y = ""
    z=""
    while i < len(x):
        if x[i] == "s" or x[i] == "S": 
            z = "$"
            y = y + z
        elif x[i-1] == " " and x[i] == "F":
            z = x[i].lower()
            y = y + z
        elif x[i-1] == " " and x[i] == "T":
            z = x[i].lower()
            y = y + z
        else:
            y = y + x[i]
        i += 1
    return y

def selectbar(x):
    i = 0
    y=""
    z=""
    while i < len(x):
        if i == 0:
            z = x[i].capitalize()
            y = y + z
        elif x[i] == "s" and x[i-1] == " ":
            z = x[i].capitalize()
            y = y + z
        elif x[i] == "c" and x[i-1] == " ":
            z = x[i].capitalize()
            y = y + z
        else:
            y = y + x[i]
        i += 1
    return y



str1 = "this is the string for the class"
str2 = capbar(str1)
str3 = spacebar(str2)
str4 = moneybar(str2)
str5 = selectbar(str1)


print("Original String: " + str(str1))
print("Part 1: " + str(str2))
print("Part 2: " + str(str3))
print("Part 3: " + str(str4))
print("Part 4: " + str(str5))