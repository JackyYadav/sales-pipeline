# Sales Summary Script

data = [100, 250, 300, 150, 400]

total = sum(data)
average = total / len(data)
max_sale = max(data)

# Write output to a log file
with open("output_log.txt", "w") as f:
    f.write(f"Total Sales: {total}\n")
    f.write(f"Average Sale: {average}\n")
    f.write(f"Highest Sale: {max_sale}\n")

print("Script ran successfully")