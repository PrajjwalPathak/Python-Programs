#Program to find the GCD of two numbers

def gcd(a, b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    else:
        return gcd(a,b-a) 

print("Enter two numbers to find GCD: ")
a = int(input())
b = int(input())
hcf = gcd(a,b)
print("HCF = {}".format(hcf))