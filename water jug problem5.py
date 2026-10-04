a,b,t=map(int,input().split())
if a>=t or b>=t:
    while b!=0:
      a,b=b,a%b
    if t%a==0:
      print("YES")
    else:
      print("NO")        
elif a<t and b<t:
    print("N0")
else:
    print("NO")      
