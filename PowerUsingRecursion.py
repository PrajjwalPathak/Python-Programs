def power(b,p):
    if(p!=0):
        return (b*power(b,p-1))
    else:
        return 1

b = int(input("Enter Base: "))
p = int(input("Enter Power: "))
r = power(b,p)
print("Result: {}".format(r))