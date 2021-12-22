#print right angled triangle
num = int(input("enter a number:"))
for r in range(0,num):
    for t in range(0,r+1):
        print("*", end ="")
    print()