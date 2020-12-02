#Program to find the GCD of multiple numbers
from array import *

def gcd(a, b):
    if(a==0):
        return b
    else:
        return gcd(b%a,a)

def gcdMultiple(a, n):
    hcf = 1
    for i in range(n-1):
        hcf = gcd(a[i],a[i+1])
    return hcf


print("Enter n: ")
n = int(input())
print("Enter n numbers to find GCD: ")
a = [0]*n
for i in range(0,n):
    a[i]=int(input())
hcf = gcdMultiple(a,n)
print("HCF = {}".format(hcf))