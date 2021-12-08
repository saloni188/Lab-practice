x = input("are you a male or female?:m or f :")
if x == "f":
    print("you will work only in urban areas.")
elif x == "m":
    y=int(input("enter your age:"))
    if y >= 20 and y <=40:
        print("you can work anywhere you like.")
    elif y >= 40 and y <=60:
        print("you will work only in urban areas.")
    else:
        print("error")

else:
    print("error")