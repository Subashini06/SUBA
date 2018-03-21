s = 0
r=int(input("Enter a number:"))
temp = r
while temp > 0:
   digit = temp % 10
   s += digit ** 3
   temp //= 10
if r == s:
   print(r,"is an Armstrong number")
else:
   print(r,"is not an Armstrong number")
