# Write a loop using enumerate() that prints only the sales greater than 10,000, along with their index.

sales = [8000, 15000, 9000, 22000]
for idx,sale in enumerate(sales) : 
    if(sale > 10000) : print(idx, sale)