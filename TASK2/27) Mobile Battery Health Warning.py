battery = int(input("Enter initial battery percentage: "))
drop = int(input("Enter hourly drop: "))

if battery < 20:
    print(0)
else:
    hours = 0
    while battery >= 20:
        battery = battery - drop
        hours = hours + 1
    print(hours)