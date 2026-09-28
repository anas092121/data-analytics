sales = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 18000
}

total = 0

for product, amount in sales.items():
    total = total + amount

print(total)