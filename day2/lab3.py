#N students take K apples and distribute them evenly
#how many apples will each student get and how many will remain in basket
N=int(input("enter the number of students:"))
K=int(input("enter the number of apples in basket:"))
student=K / N
remaining=K % N
print("the number of apples for each student is :", student)
print("the number of remaining apples in the basket:", remaining)