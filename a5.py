#A
def length(str1):
	c=0
	for i in str1:
		c=c+1
	return c
	
n=int(input("Enter the number of string:"))
list1=[]
list2=[]
for i in range(0,n):
	p=str(input("Enter your string:"))
	list1.append(p)
	list2.append(length(p))
m=max(list2)
ind=list2.index(m)
l=list1[ind]
print("Word with longest string:",l)

#B frequency
str1=str(input("Enter the string:"))
char1=input("Enter the character:")
fre=0
for i in range(len(str1)):
	if str1[i]==char1:
		fre=fre+1
print("The letter",char1,"occures",fre,"times in",str1)

#c palindrome
str1=str(input("Enter the string:"))
str2=" "
for i in str1:
	str2=i+str2
if str2==str1:
	print("Given string is not palindrome")
else:
	print("Given string is palindrome")
	
#d index 

list1=[]
string="Artificial intelligence is growing field in india"
string1=string.split()
print(string1)
result=string1.index('intelligence')
print(result)

#e count occurences
s={}
for i in s:	
	if i in s:
		s[i]+=1
	else:
		s[i]=1
print("Count of each word is:",s)
