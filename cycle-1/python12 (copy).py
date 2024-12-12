list1=[number.strip() for number in input("enter 3 numbers(comma seperated[list1]:").split(",")]
list2=[number.strip() for number in input("enter 3 numbers(comma seperated[list2]:").split(",")]

if(len(list1)==len(list2)):
	print("length is same")
else:
	print("length is not same")
if(list1.sort()==list2.sort()):
	print("sum is same")
else:
	print("sum is different")
print("the same values in  both list are:");set(list1)&set(list2)
