#Wade Willms
#Assignment 5
#Question 3 Parts 1 and 2
#Letter/Number/Symbol Counter

def letters(j):
	i = 0
	count = 0
	while i < len(j):
		if j[i].isalpha():
			count += 1
		i+=1
	return count
			
def numbers(k):
	i = 0
	count = 0
	while i < len(k):
		if k[i].isdigit():
			count += 1
		i+=1
	return count
	
def symbols(l, n, s):
	return len(s) - n - l
	

str1 = "P@#yn26at^&i5ve"

lCount = letters(str1)
nCount = numbers(str1)
sCount = symbols(lCount,nCount,str1)



print("Question 1")
print("letters: " + str(lCount))
print("Numbers: " + str(nCount))
print("Symbols: " + str(sCount))


#PART 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def symcut(a):
	i=0
	b=""
	while i < len(a):
		if a[i].isalpha() or a[i] == ' ':
			b = b + a[i]
			i += 1
		else:
			i+=1
	return b
	
str2 =  "/*Jon is @developer & musician"	
str3 = symcut(str2)

print("Question 2")
print("Original String: " + str2)
print("Modified String: " + str3)


#PART 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

















