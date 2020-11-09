#Program to find largest of 3 numbers

print("Enter 3 numbers to compare: ")
a,b,c = input().split()
print(type(a))
if(a>b):
    if(a>c):
        print("{} is the largest number".format(a))
    else:
        print("{} is the largest number".format(c))
        
else:
    if(b>c):
        print("{} is the largest number".format(b))
    else:
        print("{} is the largest number".format(c))
