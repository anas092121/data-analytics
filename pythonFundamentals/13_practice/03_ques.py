# Write a function called total_sales that:
# Takes the dictionary as a parameter.
# Returns the total of all sales.
# Then call the function and print the result.

def total_sales(sales):
    total = 0
    for prod, amount in sales.items():
        total += amount
    return total   


sales = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 18000
}

result = total_sales(sales)
print(result)