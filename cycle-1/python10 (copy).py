
age=int(input("enter the age"))
if age<10:
	print("ticket rate is 7")
elif 10<=age<60:
	print("ticket rate is 10")
elif age>60:
	print("ticket rate is 5")
else:
	print("invalid entry")
