# Sales Summary Script
# This will be automated later with cron

data = [100, 250, 300, 150, 400]

total = sum(data)
average = total / len(data)

print(f"Total Sales: {total}")
print(f"Average Sale: {average}")

max_sale = max(data)
print(f"Highest Sale: {max_sale}")