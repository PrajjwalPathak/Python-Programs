#Program to calculate the sum of natural numbers till n 

n=int(input("Enter n to find sum of n natural numbers:\n"))
Sum=0
for i in range(n+1):
    Sum = Sum + i
print("Sum is "+str(Sum))

