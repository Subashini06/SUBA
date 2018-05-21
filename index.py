s=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
  a=int(input("Enter the element:"))
  s.append(a)
for i in range(0,n):
  print("The index of the element",s[i],"is",i)
