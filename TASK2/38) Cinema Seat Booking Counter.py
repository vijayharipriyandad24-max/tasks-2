seats = int(input("Enter total seats: "))
bookings = int(input("Enter number of bookings: "))

for i in range(bookings):
    if seats > 0:
        print("BOOKED")
        seats = seats - 1
    else:
        print("HOUSEFULL")

if seats > 0:
    print("Remaining seats:", seats)