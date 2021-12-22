#find the max of three numbers 
def max(a, b, c):
    if a>b:
        if a>c:
            ans=a
        else:
            ans=c
    elif b>c:
        ans = b
    else:
        ans= c
    print("the greatest answer is {}" . format(ans))
max(1,2,3)