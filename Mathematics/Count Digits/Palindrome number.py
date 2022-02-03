# A palindromic number is a number (such as 16461) that remains the same when its digits are reversed

def ispalindrome(n):
    res=0
    temp=n
    while(n!=0):
        rem=n%10
        res=res*10+rem
        n=n//10
    
    if(temp==res):
        return True
    else:
        return False
n=int(input())
print(ispalindrome(n))
    
