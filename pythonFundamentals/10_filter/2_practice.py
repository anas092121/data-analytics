# Use filter() + lambda to multiply only transactions greater than 1000 by 2


transactions = [500, 1500, 800, 2500, 3000]

result = list(
    map(lambda x : x*2, 
        filter(lambda x : x > 1000 , transactions))
)

print(result)
