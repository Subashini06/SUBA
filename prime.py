N=int(input("Enter the number:"))
if(N>1):
  for i in range(2,N):
    if(N%i==0):
       print(" not a Prime")
       break
    
  else:
     print(" prime")
else:
  print("Not a prime ")
