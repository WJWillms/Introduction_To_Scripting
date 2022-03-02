#Wade Willms
#Assignment 5
#Question 2
#Vowel Counter

def vcount(j):
	i = 0
	count = 0
	while i < len(j):
		if j[i] == 'A' or j[i] == 'a':
			count += 1
		elif j[i] == 'E' or j[i] == 'e':
			count += 1
		elif j[i] == 'I' or j[i] == 'i':
			count += 1 
		elif j[i] == 'O' or j[i] == 'o':
			count += 1
		elif j[i] == 'U' or j[i] == 'u':
			count += 1
		i += 1
	return count
def ccount(k):
	i = 0
	count = 0
	while i < len(k):
		if k[i] == 'A' or k[i] == 'a':
			i += 1
		elif k[i] == 'E' or k[i] == 'e':
			i += 1
		elif k[i] == 'I' or k[i] == 'i':
			i += 1 
		elif k[i] == 'O' or k[i] == 'o':
			i += 1
		elif k[i] == 'U' or k[i] == 'u':
			i += 1
		else:
			count += 1
			i +=1
	return count


x = (input("Enter a string: "))

v = vcount(x)
c = ccount(x)

print("Vowels: " + str(v))
print("Consonants: " + str(c))