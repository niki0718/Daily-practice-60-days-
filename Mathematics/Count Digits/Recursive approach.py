def countnum(n):
    if n//10==0:
        return 1
    else:
        return 1+countnum(n//10)
    
n=int(input())
print(countnum(n))
