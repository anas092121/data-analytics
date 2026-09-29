# Union | → everyone from both sets
# Intersection & → common customers
# Difference - → customers in one set but not the other



# Union - combines the elements from both sets and automatically removes duplicates
# syntax - setA | setB
customers_a = {"Anas", "Rahul", "Aman", "Vikas"}
customers_b = {"Aman", "Vikas", "Rohit", "Priya"}
all_customers = customers_a | customers_b
print(all_customers)



# Intersection - the elements that exist in both sets
# syntax - setA & setB
january = {"A", "B", "C", "D"}
february = {"C", "D", "E", "F"}
common = january & february
print(common)



# Difference - gives you elements that are in the first set but NOT in the second
# syntax - setA - setB
result = january - february
print(result)