n = int(input("Enter number: "))

temp = n
digit_sum = 0
digit_product = 1

while temp > 0:
    digit = temp % 10
    digit_sum = digit_sum + digit
    digit_product = digit_product * digit
    temp = temp // 10

if digit_sum % 2 == 0 and digit_product % 3 == 0:
    print("VALID")
else:
    print("INVALID")