n = int(input("Enter number of days: "))

total_rainfall = 0
for i in range(n):
    rainfall = float(input("Enter rainfall: "))
    total_rainfall = total_rainfall + rainfall

average = total_rainfall / n

print(f"{average:.2f}")