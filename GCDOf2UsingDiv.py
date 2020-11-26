#Program to find the GCD of two numbers using divisibility test

def gcd(a, b):
    c=0, hcf=1
    if(a==b):
        hcf = a
    if(a>b):
        c = b
    else:
        c = a
    for i in range(1,c+1,1):
        if(a%i==0 and b%i==0):
            hcf = i
    return hcf

print("Enter two numbers to find GCD: ")
a = int(input())
b = int(input())
hcf = gcd(a,b)
print("HCF = {}".format(hcf))