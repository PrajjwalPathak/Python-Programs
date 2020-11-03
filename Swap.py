#Program to swap two numbers

a=int(input("Enter 1st number: "))
print("The number is",a)

b=int(input("Enter 2nd number: "))
print("The number is",b)
t=a
a=b
b=t

print("After Swaping: a = {}   b = {}".format(a,b))
