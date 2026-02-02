hour = int(input("Enter hour (0-23): "))

if hour >= 9 and hour <= 21:
    print("OPEN")
else:
    print("CLOSED")