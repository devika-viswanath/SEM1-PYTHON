
lst=[]
size=int(input("enter the list size"))
for i in range(0,size):
	a=int(input("enter value: "))
	lst.append(a)
print(lst)
val=list(map(lambda x:2**x,lst))
print(val)
