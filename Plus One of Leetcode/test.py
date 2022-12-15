x=[]
n=int(input("Enter the size of the list:"))
for i in range(n):
    s=int(input("Enter the Number in the list:"))
    x.append(s)
z=n-1
if (x[z]==9):
    x.pop()
    x.append(1)
    x.append(0)
else:

    m=x[z]+1
    x.pop()
    x.append(m)
print(x)
