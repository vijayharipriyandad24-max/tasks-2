password = int(input("Enter password: "))

password_str = str(password)
if len(password_str) < 6:
    print("WEAK")
else:
    has_seven = False
    temp = password
    while temp > 0:
        digit = temp % 10
        if digit == 7:
            has_seven = True
            break
        temp = temp // 10
    
    if has_seven:
        print("STRONG")
    else:
        print("WEAK")