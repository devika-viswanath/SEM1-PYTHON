num=input("enter integers seperated by commas").split(',')
result=[]
for n in num:

	if int(n)>100:
		result.append(over)
	else:
		result.append(int(n))
print(result)
