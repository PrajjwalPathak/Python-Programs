#Program to generate multiplication table

n = int(input("Enter a number for multiplication table: "))
p = 0
for i in range(1,11,1):
    p = n*i
    print("{} x {} = {}".format(n,i,p))