# A list comprehension is a shorter way to create a list using a loop.

# syntax - [expression for item in iterable]
# syntax - [expression for item in iterable if condition]
# What do I want to put in the list? → for each item → from where


squares = [x * x for x in range(1, 6)]
print(squares)

sales = [10000, 15000, 20000]
result = [x*2 for x in sales]
print(result)



# list comprehension with a condition
newSales = [x for x in sales if x > 10000]
print(newSales)



# Expression + Condition Together
marks = [5000, 12000, 8000, 25000, 15000]
score = [x * 2 for x in marks if x > 10000]
print(score)


myList = [x/10 for x in sales if x>10000]
print(myList)