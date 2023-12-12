def pr(num):
    if num <=1:
        False
    for i in range (2,int(num**0.5),+1):
        if num%i ==0:
            return False
    return True

for num in range(50,101):
   if pr(num):
    print(num)
