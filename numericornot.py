s=str(input("EnterThe string;"))
z=len(s)
for i in s:
  if(i.isnumeric()==True):
    print("Yes")
    break
  else:
    print("NO")
    break
