# add() - adds element to set
# setName.add(value)
# if you add something that already exists, nothing changes
customers = {"A", "B", "C", "A", "B"}
customers.add("D")
print(customers)




# Removing elements from sets
# 1. remove() → error if missing
# 2. discard() → safely ignores missing element
customers.remove("A")
customers.discard("B")
# customers.remove("X")
customers.discard("X")

print(customers)
