amount = int(input("Enter amount: "))

if amount < 1000:
    final_amount = amount
elif amount <= 2999:
    final_amount = amount * 0.90
elif amount <= 4999:
    final_amount = amount * 0.80
else:
    final_amount = amount * 0.70

print(int(final_amount))