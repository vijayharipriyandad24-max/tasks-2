n = int(input("Enter number: "))

ends_with_5 = (n % 10 == 5)

has_zero = False
temp = n
while temp > 0:
    digit = temp % 10
    if digit == 0:
        has_zero = True
        break
    temp = temp // 10

if has_zero and ends_with_5:
    print("OPEN")
else:
    print("LOCKED")