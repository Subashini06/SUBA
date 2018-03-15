n=int(input("Enter the number"))
k=int(input("Enter the limit number"))
for x in range(1,n+1):
  print(x)
sum=0
while(sum<=k):
       sum +=k
       x -= 1
print("The sum is",sum)
