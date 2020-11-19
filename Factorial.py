#Program to calculate the factorial of a number

n = int(input("Enter a number: "))
i=1
f=1
for i in range(1,n+1):
    f=f*i
print("Factorial is {}".format(f))