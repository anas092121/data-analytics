def calculate_total(sales):
    print(sum(sales))

sales = [5000, 8000, 12000]
calculate_total(sales)



# default argument - If you provide a value, it replaces the default
def greet(name, city="Delhi"):
    print(name, city)

greet("Anas")
greet("Anas","Gurgaon")



# keyword arguments - can specify perimeter name when calling
# order doesn't matter when using keyword arguments
# very usefull when we don't remember the order of the arguments
greet(name = "Anas", city = "Kanpur")



# multiple parameters
def calculate_profit(sales, cost):
    return sales - cost

profit = calculate_profit(50000, 32000)
print(profit)
