n=int(input("n="))
x=0
a=int(input("please enter 0 or 1 "))
while 1:
    if a==1:
        if n==0:
            break
        print("*"*n)
        n-=1
    if a==0:
        x += 1
        if n<x:
            break
        print("*"*x)


