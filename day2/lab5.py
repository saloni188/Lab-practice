#a school decides to replace the desks in 3 classrooms.each desk sits two students.
#given the number of students in each class.print the smallest possible number of desks.
class1=int(input("enter the number of students in first class:"))
class2=int(input("enter the number of students in second class:"))
class3=int(input("enter the number of students in third class:"))
desk1=class1//2
desk2=class2//2
desk3=class3//2
remain1=class1%2
remain2=class2%2
remain3=class3%2
total_desk=desk1+desk2+desk3+remain1+remain2+remain3
print("the total number of desk to be purchased is :", total_desk)