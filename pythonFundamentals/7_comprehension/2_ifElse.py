# [expression_if_true if condition else expression_if_false for item in iterable]


sales = [5000, 15000, 8000, 20000]
result = ["High" if x > 10000 else "Low" for x in sales]
print(result)