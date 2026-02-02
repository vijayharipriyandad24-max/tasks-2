token = int(input("Enter token number: "))

if token % 4 == 0 and token % 100 != 0:
    print("ENTRY")
else:
    print("NO ENTRY")