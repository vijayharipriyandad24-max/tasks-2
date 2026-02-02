n = int(input("Enter number: "))

count = 0

for floor in range(1, n + 1):
    has_four = False
    temp = floor
    
    while temp > 0:
        digit = temp % 10
        if digit == 4:
            has_four = True
            break
        temp = temp // 10
    
    if not has_four:
        count = count + 1

print(count)