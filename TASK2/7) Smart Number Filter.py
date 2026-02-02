n =int(input("Enter a number: "))
total=0
while n>0:
    d=n%10
    if d>1:
        is_prime=True
        for i in range(2,d):
           if d%i==0:
              is_prime=False
              break
        if is_prime:
           total =total+d
        n=n//10
print(total)
    