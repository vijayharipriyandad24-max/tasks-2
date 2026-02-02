n = int(input("Enter number: "))

temp = n
digit_sum = 0

while temp > 0:
    digit = temp % 10
 
    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i
    
    digit_sum = digit_sum + factorial
    temp = temp // 10

if digit_sum == n:
    print("STRONG")
else:
    print("NOT STRONG")