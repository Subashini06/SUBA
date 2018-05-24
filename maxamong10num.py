s=[]
n=int(input("Enter the range:"))
for i in range(0,n):
  a=int(input("Enter element:"))
  s.append(a)
print(s)
mx=s[0]
for i in s:
  if(i>mx):
    mx=i
print (mx)
