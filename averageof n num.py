l=[]
n=int(input("Enter the range:"))
for i in range(0,n):
  a=int(input("Enter the element"))
  l.append(a)
print(l)
s=sum(l)/len(l)
print(s)
