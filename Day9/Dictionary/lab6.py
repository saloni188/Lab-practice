#Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
num =int(input("Input a number "))
d = dict()

for x in range(1,num+1):
    d[x]=x*x

print(d) 