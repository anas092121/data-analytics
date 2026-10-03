# Create a new list containing double the value of only transactions greater than 1000.

transactions = [500, 1200, 800, 2500, 1500, 300]
result = list(map(lambda x : x * 2 ,filter(lambda x : x > 1000, transactions )))
print(result)
