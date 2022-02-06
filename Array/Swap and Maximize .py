def maxSum(arr,n):
    arr.sort()
    i=0
    j=n-1
    sum=0
    while(i<j):
        sum+=abs(arr[j]-arr[i])
        i+=1
        sum+=abs(arr[j]-arr[i])
        j-=1
    sum+=abs(arr[i]-arr[0])
    return sum
  
