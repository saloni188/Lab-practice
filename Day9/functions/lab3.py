# Write a function called showNumbers that takes a parameter called limit. 
#should print all the numbers between 0 and limit with a label to identify the even and odd numbers

def showNumbers(limit):
    for x in range(0,limit+1):
        if (x%2==0):
            print ("Even")
        else:
            print("Odd")
showNumbers(5)