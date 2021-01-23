#Program to find if a number is prime or not

n = int(input("Enter a number: "))
flag=0

if(n==0 or n==1):
    print("Not Prime")
elif(n==2 or n==3):
    print("Prime")
else:
    for i in range(2,n//2):
        flag==1
        break
    if(flag==0):
        print("Prime")
    else:
        print("Not a Prime")