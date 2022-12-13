a=[]
n=int(input("Enter the size of list1:"))
for i in range(n):
    s=int(input("Enter the element in the list1:"))
    a.append(s)

b=[]
m=int(input("Enter the size of list2:"))
for i in range(m):
    s=int(input("Enter the element in the list2:"))
    a.append(s)
c=a+b
c.sort()
# z=0
x=len(c)
print(c)
if(x%2==0):
    med=float((c[(x-1)//2]+c[x//2]))/2.0
    print(med)

else:
    med=(x+1)//2
    print(c[med-1])
