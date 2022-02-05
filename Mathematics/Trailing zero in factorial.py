def fact(n):
  res=1
  for i in range(1,n+1):
    res=res*i
  count=0
  while(res%10==0):
      count+=1
      res=res//10
  return count
    
