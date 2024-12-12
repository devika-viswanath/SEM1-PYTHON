colorlist1=input("enter colors for list1 in lowercase seperate by space:")
colorlist2=input("enter colors for list2 in lowercase seperate by space :")
color1=colorlist1.split()
color2=colorlist2.split()
newlist=[color for color in color1 if color not in color2]
print(f"list of colors from list1 and not contained in list2 are:{newlist}")
