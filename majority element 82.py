def maj():
    for i in range(len(arr)):
        if arr.count(arr[i])>n/2:
            return arr[i]
    return -1
n=int(input())
arr=list(map(int,input().split()))            
result=maj()
print(result)                    
        
