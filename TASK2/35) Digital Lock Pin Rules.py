pin = int(input("Enter pin: "))

if pin < 1000 or pin > 9999:
    print("ACCESS DENIED")
else:
    digit_sum = 0
    temp = pin
    while temp > 0:
        digit_sum = digit_sum + (temp % 10)
        temp = temp // 10
    
    if digit_sum > 15:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")