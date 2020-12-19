#Program to find reverse of a number

def reverse(n):
    rev = 0
    while(n!=0):
        rem = n%10
        rev = rev*10 + rem
        n = n//10
    return rev
    
print("Enter Number: ")
n = int(input())
r = reverse(n)
print("Reversed Number = {}".format(r))