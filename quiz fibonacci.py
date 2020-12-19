def fabonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonacci(n-1)+fabonacci(n-2)
number=int(input())
print(fabonacci(number))

