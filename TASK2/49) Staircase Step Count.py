n = int(input("Enter total stairs: "))
k = int(input("Enter step size: "))

if n % k == 0:
    steps = n // k
else:
    steps = (n // k) + 1

print(steps)