#Program to find the LCM of multiple numbers

import array

def lcm(a,b):
    if(a==0 or b==0):
        return 0 
    else:
        max = a if a>b else b
        while(True):
            if(max%a==0 and max%b==0):
                return max
            max = max + 1

def lcmOfMulti(A,n):
    for i in range(0,n-1,1):
        for j in range(1,n,1):
            A[j] = lcm(A[i],A[j])
    return A[n-1]

print("Enter n: ")
n = int(input())
print("Enter n numbers to find LCM: ")
A = [0]*n
for i in range(0,n):
    A[i]=int(input())
l = lcmOfMulti(A,n)
print("LCM = {}".format(l))