#to count the number of even and odd numbers from a series of numbers
even, odd= 0, 0

for i in range(1,200): 

    if i % 2 == 0: 

        even += 1

    else: 

        odd+= 1          

print("Even : ", even) 

print("Odd : ", odd)