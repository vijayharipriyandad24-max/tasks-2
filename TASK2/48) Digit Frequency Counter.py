n = int(input("Enter number: "))
d = int(input("Enter digit to count: "))

count = 0
temp = n
while temp > 0:
    digit = temp % 10
    if digit == d:
        count = count + 1
    temp = temp // 10

print(count)