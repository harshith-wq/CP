n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
c=sorted(arr1+arr2)
print(*c)
          
