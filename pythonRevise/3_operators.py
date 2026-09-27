# comditional operators

10 > 5      # True
10 < 5      # False
10 == 10    # True
10 != 5     # True
10 >= 10    # True
10 <= 9     # False

sales = 50000
print(sales > 30000)
print(sales == 50000)
print(sales < 10000)

orders = 25
print(orders > 20)
print(orders == 20)
print(orders != 20)


# logical 

sales = 45000
orders = 15

print(sales > 40000 and orders > 20)
print(sales > 40000 or orders > 20)
print(not (sales > 40000))