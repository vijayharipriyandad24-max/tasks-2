n = int(input("Enter number: "))

reversed_num = 0
temp = n
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10

if reversed_num < 2:
    print("NOT PRIME")
else:
    is_prime = True
    for i in range(2, int(reversed_num ** 0.5) + 1):
        if reversed_num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("PRIME")
    else:
        print("NOT PRIME")