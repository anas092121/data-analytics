# map() applies a function to every item in a sequence
# Take every item → apply this operation → create the results


sales = [10000, 15000, 20000]
result = list(map(lambda x: x * 2, sales))
print(result)