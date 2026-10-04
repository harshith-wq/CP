n=int(input())
arr=list(map(int,input().split()))
max_sum=arr[0]
for i in range(n):
    current_sum=0
    for j in range(i,n):
        current_sum+=arr[j]
        if current_sum>max_sum:
            max_sum=current_sum
print(max_sum)            
