s=int(input("Enter the number:"))
if(s>1):
  for i in range(2,s):
    if(s%i==0):
       print(" composite")
       break
  else:
     print("not a composite")
else:
  print("composite ")
