# Sales Summary Script
# This will be automated later with cron

data = [100, 250, 300, 150, 400]

total = sum(data)
average = total / len(data)

print(f"Total Sales: {total}")
print(f"Average Sale: {average}")