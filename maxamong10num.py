l=[]
n=int(input("Enter the range:"))
for i in range(0,n):
  a=int(input("Enter element:"))
  l.append(a)
print(l)
mx=l[0]
for i in l:
  if(i>mx):
    mx=i
print (mx)
