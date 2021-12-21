#to multiply all the items in a list
import math
def multiply_list(list):
     return math.prod(list)
     

list1 = [3, 2, 5, 4, 8, 9, 10]
print(list1)
print("product: ") 
print(multiply_list(list1))