n = int(input("Enter ticket number: "))

digit_sum = 0
temp = n
while temp > 0:
    digit_sum = digit_sum + (temp % 10)
    temp = temp // 10

if digit_sum % 9 == 0:
    print("VALID")
else:
    print("INVALID")