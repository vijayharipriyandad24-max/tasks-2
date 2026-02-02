liters = float(input("Enter liters: "))
price = float(input("Enter price per liter: "))

total_bill = liters * price

last_digit = int(total_bill) % 10
if last_digit <= 4:
    rounded_bill = int(total_bill) - last_digit
else:
    rounded_bill = int(total_bill) + (10 - last_digit)

print(rounded_bill)