#find BMI of a person where take mass and height as input
#BMI = mass in kg / (height in m)2
m=int(input("enter the mass of person in kg:"))
h=int(input("enter the height of person in meter:"))
BMI=(m/(h*h))
print(f"the BMI value of a person is {BMI}")