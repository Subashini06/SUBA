a=int(input("Enter the hr:"))
b=int(input("Enter the min:"))
c=int(input("Enter hr value of the second"))
d=int(input("Enter the minute of the second"))
if(b>60 and d>60):
  a=a-1
  c=c-1
print(a-c,b-d)
