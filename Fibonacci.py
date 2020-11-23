#Program to generate multiplication table

t1=1
t2=1
t3=0
n = int(input("Write a positive number to print Fibonaci series: "))
if(n==1):
    print(t1)
elif(n==2):
    print("{} {}".format(t1,t2))
else:
    print("{} {} ".format(t1,t2),end="")
    for i in range(2,n,1):
        t3 = t1+t2
        print("{} ".format(t3),end="")
        t1=t2
        t2=t3