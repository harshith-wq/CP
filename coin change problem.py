V,N=map(int,input().split())
coins=list(map(int,input().split()))

INF=10**9
dp=[INF]*(V+1)
parent=[-1]*(V+1)
dp[0]=0

for i in range(1,V+1):
    for coin in coins:
        if coin<=i and dp[i-coin]+1<dp[i]:
            dp[i]=dp[i-coin]+1
            parent[i]=coin

if dp[V]==INF:
    print(-1)
else:
    result=[]
    x=V
    while x>0:
        result.append(parent[x])
        x-=parent[x]
    print(dp[V])
