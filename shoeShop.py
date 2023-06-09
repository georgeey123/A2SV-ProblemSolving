from collections import Counter

n = int(input())  
shoe_sizes = Counter(map(int, input().split()))  # list of shoe sizes

m = int(input()) 
total_earnings = 0

for _ in range(m):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        total_earnings += price
        shoe_sizes[size] -= 1

print(total_earnings)
