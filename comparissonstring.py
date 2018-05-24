s=str(input("Enter the string:"))
t=str(input("Enter the second string:"))
n=len(s) and len(t)
r=0
for i in range(0,n):
  if(s[i]==t[i]):
    s=t
  print(s)
else:
  for i in range(0,n):
    if(s[i]>t[i]):
      r+=1
    print(t)
