names=["Devika","Osheen","Varsha","Lekshmi"]
freequency=0
for name in names:
	freequency+=name.lower().count("a")
print(f"occurance of 'a' in list is {freequency}" )
