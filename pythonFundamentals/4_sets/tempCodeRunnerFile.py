january = {"A", "B", "C", "D", "E"}
february = {"C", "D", "E", "F", "G"}
common = january & february
new_customers = february - january
all_customers = january | february
print(common)
print(new_customers)
print(len(all_customers))