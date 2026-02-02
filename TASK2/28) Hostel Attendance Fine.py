attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    fine = 0
else:
    fine = (75 - attendance) * 10

print(fine)