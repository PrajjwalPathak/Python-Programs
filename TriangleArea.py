#Program to calculate the area of triangle
import math as m

print("Enter the length of the sides: ")
a=int(input())
b=int(input())
c=int(input())
if(a+b>c and a+c>b):
    S=(a+b+c)/2
    A=m.sqrt(S*(S-a)*(S-b)*(S-c))
    print("Area is {:0.3f}".format(A))
else:
    print("Invalid Triangle")

