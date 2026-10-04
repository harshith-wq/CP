def egcd(a,b):
    if b==0:return a,1,0
    d,x,y=egcd(b,a%b)
    return d,y,x-(a//b)*y

A,B=map(int,input().split())
D,x,y=egcd(A,B)
p=B//D
q=A//D
k1=(-x)//p
k2=y//q
c=set(range(k1-2,k1+3))|set(range(k2-2,k2+3))
best=None

for k in c:
    X=x+k*p
    Y=y-k*q
    v=abs(X)+abs(Y)
    if best is None or v<best[0] or (v==best[0] and X<best[1]):
        best=(v,X,Y)

print(best[1],best[2],D)

