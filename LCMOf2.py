#Program to find LCM of 2 numbers

def lcm(a,b):
    if(a==0 or b==0):
        return 0 
    else:
        max = a if a>b else b
        while(True):
            if(max%a==0 and max%b==0):
                return max
            max = max + 1

print("Enter 2 numbers to find LCM: ")
a = int(input())
b = int(input())
l = lcm(a,b)
print("LCM = {}".format(int(l)))