str=input("enter a string:")
str2=str.lower()
count={}
for char in str2:
	if char in count:
		count[char]+=1
	else:
		count[char]=1
print(count)
