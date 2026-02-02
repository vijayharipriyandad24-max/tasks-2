balance = int(input("Enter balance: "))

if balance < 10000:
    annual_rate = 0.03
elif balance <= 50000:
    annual_rate = 0.05
else:
    annual_rate = 0.07

monthly_interest = (balance * annual_rate) / 12

print(f"{monthly_interest:.2f}")