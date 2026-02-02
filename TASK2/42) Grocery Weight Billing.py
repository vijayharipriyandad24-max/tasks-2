weight = float(input("Enter weight in kg: "))
price = float(input("Enter price per kg: "))

total_cost = weight * price

if weight > 10:
    final_bill = total_cost * 0.95  # 5% discount
else:
    final_bill = total_cost

print(f"{final_bill:.2f}")