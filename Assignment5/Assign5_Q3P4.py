#Wade Willms
#Assignment 5
#Question 3 Part 3
#Replace "-" with " "

def spacebar(x):
    i = 0
    y=""
    while i < len(x):
        if x[i] == "a" or x[i] == "A":
            y = y + x[i]
            i += 1
        elif x[i] == "e" or x[i] == "E":
            y = y + x[i]
            i += 1
        elif x[i] == "i" or x[i] == "I":
            y = y + x[i]
            i += 1
        elif x[i] == "o" or x[i] == "O":
            y = y + x[i]
            i += 1
        elif x[i] == "u" or x[i] == "U":
            y = y + x[i]
            i += 1
        elif x[i] == " " or x[i] == ",":
            y = y + x[i]
            i += 1
        else:
            i += 1
    return y

str3 = "Hello,have a good day"
str4 = spacebar(str3)
print("Original String: " + str3)
print("Modified String: " + str(str4))