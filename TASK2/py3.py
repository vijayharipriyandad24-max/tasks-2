n=int(input("n:"))
t=n
c=0
while t!=0:
  c=c+t%10
  t=t//10
if c%3==0 and (n%10)%2==0:
  print("valid")
else:
  print("invalid")