# zip() is used to combine corresponding elements from two or more lists.

# First item + first item → pair
# Second item + second item → pair
# Third item + third item → pair .........


names = ["Anas", "Rahul", "Amit"]
sales = [20000, 15000, 18000]
result = list(zip(names, sales))
print(result)



products = ["Laptop", "Phone", "Tablet"]
prices = [55000, 25000, 18000]
result = list(zip(products, prices))
print(result)