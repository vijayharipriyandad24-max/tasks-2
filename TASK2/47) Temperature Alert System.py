n = int(input("Enter number of hours: "))

alert = False
for i in range(n):
    temp = int(input("Enter temperature: "))
    if temp > 45:
        alert = True
        break

if alert:
    print("ALERT")
else:
    print("SAFE")