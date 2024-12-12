from Graphics.rectangle import *
from Graphics.circle import *
from Graphics.threeDGraphics.cuboid import *
from Graphics.threeDGraphics.sphere import *

print("Rectangle")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth :"))
print("Area of rectangle:",RectArea(l,b))
print("Area of rectangle:",RectPerimeter(l,b))

print("Circle")
r=int(input("Enter the radius :"))
print("Circle Area:",CircleArea(r))
print("Circle Perimeter:",CirclePerimeter(r))

print("Cuboid")
l=int(input("Enter the length:"))
w=int(input("Enter the width :"))
h=int(input("Enter the height:"))
CuboidArea(l,w,h)
CuboidPerimeter(l,w,h)


print("Sphere")
r=int(input("Enter the radius for :"))
print("Sphere Area:",SphereArea(r))
print("Sphere volume:",SpherePerimeter(r))
