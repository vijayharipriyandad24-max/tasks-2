late_minutes = int(input("Enter late minutes: "))

if late_minutes <= 10:
    penalty = 0
elif late_minutes <= 30:
    penalty = 50
else:
    penalty = 100

print(penalty)