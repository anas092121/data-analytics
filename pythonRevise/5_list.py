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
removed = income.pop() #removes last value
print(removed)
print(income)



# len - tells you how many elements are in a list
count = [1,2,3,4,5]
lengthOfList = len(count)
print(lengthOfList)



# slicing - lest you take a portion of a list (subarray)
# list[start:end] - end is not included
carSales = [10, 15, 80, 20, 12]
print(carSales[0:4])
print(carSales[:4])
print(carSales[1:])
print(carSales[-3:])
print(carSales[-3:-1])



# sort - arranges a list in ascending order / changes the original list
values = [15000, 8000, 22000, 10000]
values.sort()
print(values)
values.sort(reverse=True) # desceding order
print(values)



# reverse - reverses the current order of the list
data = [10000, 20000, 80000, 40000]
data.reverse()
print(data)



# count - frequncy of an element in a list
diatance = [10000, 15000, 10000, 20000, 10000]
print(diatance.count(10000))



# index - tells the index of first occurance index of a value in a list
transactions = [100, 200, 100, 300, 100]
print(transactions.index(100))