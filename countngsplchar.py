x=str(input("Enter the string:"))
digit=0
letter=0
others=0
t=len(x)
for i in range(0,t):
  if x[i].isnumeric():
    digit += 1
  elif x[i].isalpha():
    letter+=1
  else:
    others+=1
print(others)
