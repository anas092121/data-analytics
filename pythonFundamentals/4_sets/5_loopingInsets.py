# order will be random because set is unordered

customers = {"A", "B", "C"}
for customer in customers:
    print(customer)


# practice - implement difference without using - sign
saetA = {"A", "B", "C", "D"}
setB = {"C", "D", "E", "F"}
ans = []
for char in saetA:
    if char in setB:
        pass
    else:
        ans.append(char)
print(ans)        



# practice
january = {"A", "B", "C", "D", "E"}
february = {"C", "D", "E", "F", "G"}
common = january & february
new_customers = february - january
all_customers = january | february
print(common)
print(new_customers)
print(len(all_customers))