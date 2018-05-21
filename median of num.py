s=[]
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    a=int(input("Enter the elements:"))
    s.append(a)
h=sum(s)/float(len(s))
print(h)
