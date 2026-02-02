batch = int(input("Enter batch number: "))

first_digit = int(str(batch)[0])
if first_digit == 0:
    print("INVALID")
else:
    last_digit = batch % 10
    if last_digit % 2 == 0:
        print("VALID")
    else:
        print("INVALID")