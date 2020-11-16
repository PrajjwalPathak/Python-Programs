#Program to tell if the year is a Leap Year or not

year = int(input("Enter a year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("It is a Leap year")
        else:
            print("It is not a Leap year")
    else:
        print("It is a Leap year")
else:
    print("It is not a Leap year")