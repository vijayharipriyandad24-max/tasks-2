days = int(input("Enter late days: "))

if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = 5 * 2 + (days - 5) * 3
else:
    fine = 5 * 2 + 5 * 3 + (days - 10) * 5

print(fine)