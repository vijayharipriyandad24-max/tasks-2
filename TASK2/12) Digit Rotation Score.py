n = int(input("Enter number: "))

num_str = str(n)
length = len(num_str)

score = 0

for i in range(length):
    rotated = num_str[i:] + num_str[:i]
    rotated_num = int(rotated)
    
    score = score + rotated_num

print(score)