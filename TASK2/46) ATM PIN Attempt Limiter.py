correct_pin = int(input("Enter correct PIN: "))
attempt1 = int(input("Enter attempt 1: "))
attempt2 = int(input("Enter attempt 2: "))
attempt3 = int(input("Enter attempt 3: "))

if attempt1 == correct_pin or attempt2 == correct_pin or attempt3 == correct_pin:
    print("ACCESS GRANTED")
else:
    print("CARD BLOCKED")