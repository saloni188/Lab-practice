a=int(input("number of classes held:"))
b=int(input("number of classes attended"))
c=(b/a)*100
print(f"you are {c} % present in a classes.")
if c >= 75:
    print("you are allowed.")
else:
    print("you are not allowed.")