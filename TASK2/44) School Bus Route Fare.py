distance = int(input("Enter distance in km: "))

if distance <= 5:
    fare = distance * 10
elif distance <= 15:
    fare = 5 * 10 + (distance - 5) * 8
else:
    fare = 5 * 10 + 10 * 8 + (distance - 15) * 6

print(fare)