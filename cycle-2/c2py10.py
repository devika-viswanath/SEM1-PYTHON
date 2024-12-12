n=int(input("enter no: of integers to input:"))
listed=[]
for i in range(n):
        num=int(input("enter integer:"))
        if num%2!=0:
                listed.append(num)
print(f"newlist:{listed}")


