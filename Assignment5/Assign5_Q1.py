#Wade Willms
#Assignment 5
#Question 1
#Morse Code

x = (input("Enter something to translates it into Morse Code: "))
y = " "

i=0
while i < len(x):
	if x[i] == 'a' or x[i] =='A':
		y = y + ". - "
		i+=1
	elif x[i] == 'b' or x[i] =='B':
		y = y + "- . . . "
		i+=1
	elif x[i] == 'c' or x[i] =='C':
		y = y + "- . - . "
		i+=1
	elif x[i] == 'd' or x[i] =='D':
		y = y + "- . . "
		i+=1
	elif x[i] == 'e' or x[i] =='E':
		y = y + ". "
		i+=1
	elif x[i] == 'f' or x[i] =='F':
		y = y + ". . - . "
		i+=1
	elif x[i] == 'g' or x[i] =='G':
		y = y + "- - . "
		i+=1
	elif x[i] == 'h' or x[i] =='H':
		y = y + ". . . . "
		i+=1
	elif x[i] == 'i' or x[i] =='I':
		y = y + ". . "
		i+=1
	elif x[i] == 'j' or x[i] =='J':
		y = y + ". - - - "
		i+=1
	elif x[i] == 'k' or x[i] =='K':
		y = y + "- . - "
		i+=1
	elif x[i] == 'l' or x[i] =='L':
		y = y + ". - . . "
		i+=1
	elif x[i] == 'm' or x[i] =='M':
		y = y + "- - "
		i+=1
	elif x[i] == 'n' or x[i] =='N':
		y = y + "- . "
		i+=1
	elif x[i] == 'o' or x[i] =='O':
		y = y + "- - - "
		i+=1
	elif x[i] == 'p' or x[i] =='P':
		y = y + ". - - . "
		i+=1
	elif x[i] == 'q' or x[i] =='Q':
		y = y + "- - . - "
		i+=1
	elif x[i] == 'r' or x[i] =='R':
		y = y + ". - . "
		i+=1
	elif x[i] == 's' or x[i] =='S':
		y = y + ". . . "
		i+=1
	elif x[i] == 't' or x[i] =='T':
		y = y + "- "
		i+=1
	elif x[i] == 'u' or x[i] =='U':
		y = y + ". . - "
		i+=1
	elif x[i] == 'v' or x[i] =='V':
		y = y + ". . . - "
		i+=1
	elif x[i] == 'w' or x[i] =='W':
		y = y + ". - - "
		i+=1
	elif x[i] == 'x' or x[i] =='X':
		y = y + "- . . - "
		i+=1
	elif x[i] == 'y' or x[i] =='Y':
		y = y + "- . - "
		i+=1
	elif x[i] == 'z' or x[i] =='Z':
		y = y + "- - . . "
		i+=1
	elif x[i] == '0':
		y = y + "- - - - - "
		i+=1
	elif x[i] == '1':
		y = y + ". - - - - "
		i+=1
	elif x[i] == '2':
		y = y + ". . - - - "
		i+=1
	elif x[i] == '3':
		y = y + ". . . - - "
		i+=1
	elif x[i] == '4':
		y = y + ". . . . - "
		i+=1
	elif x[i] == '5':
		y = y + ". . . . . "
		i+=1
	elif x[i] == '6':
		y = y + "- . . . . "
		i+=1
	elif x[i] == '7':
		y = y + "- - . . . "
		i+=1
	elif x[i] == '8':
		y = y + "- - - . . "
		i+=1
	elif x[i] == '9':
		y = y + "- - - - . "
		i+=1
	elif x[i] == '.':
		y = y + ". - . - . - "
		i+=1
	elif x[i] == ',':
		y = y + "- - . . - - "
		i+=1
	elif x[i] == '?':
		y = y + ". . - - . . "
		i+=1
	elif x[i] == ' ':
		y = y + "   "
		i+=1
	else:
		y = y + "? "
		i+=1
        
print("As Morse Code: " + y)
















