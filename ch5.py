def fac(n):
    if n<0:
        raise ValueError("enter positive number")

    if n == 0:
        return 1
    else :
        return n*fac(n-1)

print(fac(-9))