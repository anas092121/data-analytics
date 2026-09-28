# pop() - removes items form dictionary
sales = {
    "Monday": 12000,
    "Tuesday": 15000,
    "Wednesday": 9000
}
sales.pop("Tuesday")
print(sales)


# get() - retreive a value using key
# dict.get(key)
retreivedValue = sales.get("Monday")
print(retreivedValue)

# when key doesn't exist - one of advantage
print(sales.get("Friday"))

# we can provide a default value when key doesn't exist
print(sales.get("Friday", 0))
print(sales.get("Friday", "Day not Found"))
