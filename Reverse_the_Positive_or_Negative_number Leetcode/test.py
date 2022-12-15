num=321
sum=0
if(num>0):
    while(num>0):
        a=num%10
        sum=sum*10+a
        num=num//10
else:
    num=num*(-1)
    while(num>0):
        a=num%10
        sum=sum*10+a
        num=num//10
    sum=sum*(-1)
print(sum)
    
    
