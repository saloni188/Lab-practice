#which accepts marks of four subjects and display total marks, percentage and grade
marks1=int(input("enter marks of first subject"))
marks2=int(input("enter marks of second subject"))
marks3=int(input("enter marks of third subject"))
marks4=int(input("enter marks of fourth subject"))
total_marks=marks1+marks2+marks3+marks4
print("your total marks obtained is:", total_marks)
percent=(total_marks/400)*100
print("your total percentage is:", percent )
if percent >70 and percent <=100:
    print("you've scored distinction")
    print("you obtained grade A")
elif percent >60 and percent <=70:
     print ("You've scored first division")
     print ("You obtained grade B")
elif percent >40 and percent <=60:
    print ("You're pass")
    print ("You obtained grade C")
else:
    print("You are fail")
    print ("You obtained grade D")