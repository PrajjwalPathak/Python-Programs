#Program to find LCM of 2 numbers

def gcd(a,b):
    if(a==0):
        return b 
    else:
        return gcd(b%a,a)

print("Enter 2 numbers to find LCM: ")
a = int(input())
b = int(input())
hcf = gcd(a,b)
lcm = a*b/hcf
print("LCM = {}".format(int(lcm)))