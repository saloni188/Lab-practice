#find the hours and minutes displayed on 24h digital clock (since midnight) by given integer
n=int(input("enter the number of minutes passed"))
time = n // 60
hours = n % 60
print("the hours passed is:", time)
print("the minutes passed is:", hours)