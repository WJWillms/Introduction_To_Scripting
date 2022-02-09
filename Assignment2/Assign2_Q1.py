#Wade Willms
#Assignment 2
#Question 1
#Star loop printer



counter = 0 #counts times through loop
starCounter = 0 #counts stars until it reaches starAmount
starAmount = 1 #Maintains numbers of stars to be printer per line
while counter < 5:
    while starCounter < starAmount:
        print("*", end=" ")
        starCounter = starCounter+1
    counter = counter + 1
    starAmount = starAmount + 1
    starCounter = 0
    print("")
    
    



counter = 5
starCounter = 0
starAmount = 1
blankCounter = 0 #Counts blanks until it reaches blankAmount
blankAmount = 4 #Maintains amounts of blanks to be printed per line
while counter > 0:
    while blankCounter < blankAmount:
        print(" ", end=" ")
        blankCounter = blankCounter+1
    blankAmount = blankAmount - 1
    blankCounter = 0
    while starCounter < starAmount:
        print("*", end=" ")
        starCounter = starCounter+1
    counter = counter - 1
    starAmount = starAmount + 1
    starCounter = 0
    print("")