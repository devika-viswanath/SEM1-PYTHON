str=input("enter a string:")
str2=str.lower()
firstchar=str2[0]
newstr=firstchar+str2[1:].replace(firstchar,"$")
print(f"new string is:{newstr}")
