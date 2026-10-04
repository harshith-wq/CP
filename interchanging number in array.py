n=int(input())
arr=list(map(int,input().split()))
largest=max(arr)
smallest=min(arr)
large_index=arr.index(largest)
small_index=arr.index(smallest)
arr[large_index],arr[small_index]=arr[small_index],arr[large_index]
print(*arr)

    
