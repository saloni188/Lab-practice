def value(x,y,z):
    if x == y or x == z or y == z:
        suma=0
        print(f"the sum of three integer:{suma}")
    else:
        suma = x+y+z
        print(f"the sum of three integer:{suma}")
x=int(input("enter a first number"))
y=int(input("enter a second number"))
z=int(input("enter a third number"))
value(x,y,z)
