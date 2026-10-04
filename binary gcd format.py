def gcd(a,b):
    if a==0:
        return b
    elif b==0:    
        return a
    elif (a&1)==0 and (b&1)==0:
        return 2*gcd(a>>1,b>>1)    
    elif (a&1)==0:
        return gcd(a>>1,b)
    elif (b&1)==0:
        return gcd(a,b>>1)
    elif a>=b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)
    return a
a,b=map(int,input().split())
print(gcd(a,b)) 
