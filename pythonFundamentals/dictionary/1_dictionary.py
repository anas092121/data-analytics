# A dictionary stores data as key → value pairs:

# dicName{
#     key : value
# }

customer = {
    "name": "Anas",
    "age": 22,
    "city": "Delhi"
}
print(customer)
print(customer["name"])


# adding and updating values 
customer["weight"] = 85 # adding value
customer["city"] = "Gurgaon" # updating value
print(customer) 



# key,value,items
# key() -> all keys 
# values() -> all values 
# items() -> key value pairs 
days = {
    "Monday": 12000,
    "Tuesday": 15000,
    "Wednesday": 9000
}
print(days.keys())
print(days.values())