n = int(input("Enter number: "))

digits_present = [False] * 10

temp = n
while temp > 0:
    digit = temp % 10
    digits_present[digit] = True
    temp = temp // 10

missing_digit = -1
for i in range(10):
    if not digits_present[i]:
        missing_digit = i
        break

print(missing_digit)