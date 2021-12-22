#given a n-digit number, find the sum of its digits
num=int(input("enter a number:"))
sumofdigits=0
for digit in str(num):
    sumofdigits += int(digit)
print(sumofdigits)