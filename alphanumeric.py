s=str(input("Enter the string"))
z=len(s)
for i in range(0,z):
  if(s[i].isalpha() or s[i].isdigit()):
    print("yes")
    break
else:
    print("no")
