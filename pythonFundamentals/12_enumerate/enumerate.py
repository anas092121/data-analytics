# enumerate() lets you loop through a list while getting both the index and the value
# for index, value in enumerate(list):


products = ["Laptop", "Phone", "Tablet"]
for i, product in enumerate(products):
    print(i, product)

print(enumerate(products))