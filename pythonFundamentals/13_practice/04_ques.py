# Write a function: def high_transactions(transactions)
# It should return a dictionary containing only transactions greater than 1000 for each customer.


def high_transactions(transactions):
    mydict = {}
    for customer, amounts in transactions.items():
        mydict[customer] = list(filter(lambda x : x > 1000 , amounts))
    return mydict    



transactions = {
    "Anas": [1200, 500, 2500],
    "Rahul": [800, 1800, 3000],
    "Amit": [400, 700, 1500]
}

result = high_transactions(transactions=transactions)
print(result)