# Creating and accessing a list
sales = [12000, 15000, 9000, 22000]
print(sales[0])
print(sales[2])
print(sales[3])


# -ve indexing
print(sales[-1])
print(sales[-2])


# append
sales.append(18000)
sales[-3] = 10000
print(sales)


# insert
# .append() adds an item at the end.
# .insert() lets you add an item at a specific position.
marks = [70, 80, 90]
marks.insert(1, 99)
print(marks)


# remove - removes an element by its value
income = [12000, 15000, 9000, 22000]
income.remove(9000)
print(income)


# pop - removes an element using its index and can also give you the removed value
removed = income.pop(2)
print(removed)
print(income)

