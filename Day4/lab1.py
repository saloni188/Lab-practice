def leapyear(year):
    if (year % 400) ==0 or (year % 100)!=0 and (year % 4)==0:
        print("is leap year")
    else:
        print("not a leap year")

year=int(input("enter a year:"))
leapyear(year)
