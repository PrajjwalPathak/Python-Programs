#Program to divide a number

D=int(input("Enter Dividend: "))
d=int(input("Enter Divisor: "))
q=D/d
r=D%d
print("Quotient: {:0.2f}".format(q))
print("Remainder: {}".format(r))