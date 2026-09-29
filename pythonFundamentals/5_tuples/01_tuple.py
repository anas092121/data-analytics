# Tuple is similar to list but it is immutable
# once created it's elements cannot be changed

sales = (12000, 15000, 9000, 18000)
print(sales[0])   # 12000
print(sales[-1])  # 18000



#  Diff bw list and tuples

# List → mutable
sales_list = [12000, 15000]
sales_list[0] = 13000   # allowed
# Tuple → immutable
sales_tuple = (12000, 15000)
sales_tuple[0] = 13000  # TypeError