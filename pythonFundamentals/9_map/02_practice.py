'''
Given:
sales = [10000, 20000, 30000]
Use map() + lambda to add 1000 to every sale  
'''

sales = [10000, 20000, 30000]
result = list(map(lambda x : x + 1000, sales))
print(result)