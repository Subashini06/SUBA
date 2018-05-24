x=str(input("Enter the string:"))
digit=0
t=len(x)
for i in range(0,t):
  if x[i].isnumeric():
    digit += 1
print(digit)
