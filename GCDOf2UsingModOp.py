#Program to find GCD of 2 numbers

def gcd(a, b):
    if(a==0):
        return b
    else:
        return gcd(b%a,a)

print("Enter two numbers to find GCD: ")
a = int(input())
b = int(input())
hcf = gcd(a,b)
print("HCF = {}".format(hcf))