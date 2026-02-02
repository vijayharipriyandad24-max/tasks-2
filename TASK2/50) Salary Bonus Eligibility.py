years = int(input("Enter years of service: "))

if years < 2:
    bonus = 0
elif years <= 5:
    bonus = 5000
elif years <= 10:
    bonus = 10000
else:
    bonus = 20000

print(bonus)