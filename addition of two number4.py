num1,num2=map(int,input().split())
while num2!=0:
    carry=num1&num2
    num1=num1^num2
    num2=carry<<1
print(num1)    
