
import math
print("quadratic eqn ax^2+bx+c")
a=float(int(input()))
b=float(int(input()))
c=float(int(input()))
d=(b*b)-(4*a*c)
if(d==0):
	print("only one root value\n")
	ans=(-b)/(2*a)
	print("x= ",ans)
elif(d>0):
	sqrtvalue=math.sqrt(d)
	ansone=(-b+sqrtvalue)/2*a
	anstwo=(-b-sqrtvalue)/2*a
	print("x1= ",ansone)
	print("x2= ",anstwo)
else:
	print("complexroot")
	sqrtvalue=math.sqrt(abs(d))/(2*a)
	print(-b/(2*a),"+i",sqrtvalue)
	print(-b/(2*a),"-i",sqrtvalue)
