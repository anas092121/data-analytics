# filter() is used to keep only the items that satisfy a condition
# map() → transform every item
# filter() → select certain items

sales = [5000, 12000, 8000, 20000]
result = list(filter(lambda x : x>10000 , sales))
print(result)