#Program to find if a number is a palindrome or not

i = int(input("Enter a number: "))
rev=0
ori=i
while(i!=0):
    rev=rev*10
    rev=rev+i%10
    i=i//10
if(rev==ori):
    print("Palindrome")
else:
    print("Not a Palindrome")