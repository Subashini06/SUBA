r=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    s=int(input("Enter element:"))
    r.append(s)
r.sort()
print(r)
