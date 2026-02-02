hours = int(input("Enter current hours: "))
minutes = int(input("Enter current minutes: "))
extra_minutes = int(input("Enter minutes to add: "))

total_minutes = minutes + extra_minutes
added_hours = total_minutes // 60
remaining_minutes = total_minutes % 60

final_hours = (hours + added_hours) % 24

print(final_hours, remaining_minutes)