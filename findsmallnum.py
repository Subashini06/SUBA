s=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    r=int(input("Enter element:"))
    s.append(r)
s.sort()
print("smallest element is:",s[0])
