#Wade Willms
#Assignment 5
#Question 3
#

def spacebar(x):
    i = 0
    y=""
    while i < len(x):
        if x[i] == "-":
            y = y + " "
        else:
            y = y + x[i]
        i += 1
    return y

str3 = "Emma-is-a-data-scientist"
str4 = spacebar(str3)
print("Original String: " + str3)
print("Modified String: " + str(str4))