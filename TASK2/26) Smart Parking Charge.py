hours = int(input("Enter parked hours: "))

if hours <= 2:
    charge = hours * 20
elif hours <= 5:
    charge = 2 * 20 + (hours - 2) * 15
else:
    charge = 2 * 20 + 3 * 15 + (hours - 5) * 10

print(charge)