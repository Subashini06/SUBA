s=int(input("Enter the number:"))
if(s>1):
  for i in range(2,s):
    if(s%i==0):
       print(" not a Prime")
       break
  else:
     print(" prime")
else:
  print("Not a prime ")
