length = int(input("Enter length: "))
width = int(input("Enter width: "))
height = int(input("Enter height: "))

if length <= 0 or width <= 0 or height <= 0:
    print("REJECTED")
else:
    total_sum = length + width + height
    if total_sum <= 150:
        print("ACCEPTED")
    else:
        print("REJECTED")