


lst = []
size = int(input("Enter no of elements : "))
for i in range(0, size):
    a = int(input("Enter the values : "))
    lst.append(a)
ans = lambda x : 3 * x
for i in range(0, size):
        print(ans(lst[i]), end = " ")
