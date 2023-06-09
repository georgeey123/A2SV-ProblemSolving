from collections import OrderedDict

N = int(input())
sales = OrderedDict()

for i in range(N):
    #reversed split for the last space.
    fruit_name, fruit_price = input().rsplit(" ", 1)  
    sales[fruit_name] = sales.get(fruit_name,0)
    sales[fruit_name] += int(fruit_price)
    
for fruit_name, net_price in sales.items():
    print(f"{fruit_name} {net_price}")
