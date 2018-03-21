a=int(input("Enter a num"))
b=int(input("Enter a num"))
for r in range(a,b):
  s = 0
  temp = r
  while temp > 0:
    digit = temp % 10
    s += digit ** 3
    temp //= 10
  if r == s:
      print(r)
