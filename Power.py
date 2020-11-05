#Program to find the pth power of a number

b=int(input("Enter base: "))
p=int(input("Enter power: "))
r=b
for i in range(p-1):
    r=r*b
print("Result: {}".format(r))