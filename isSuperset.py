a = set(map(int, input().split()))
n = int(input())

is_superset = True

for i in range(n):
    subset = set(map(int, input().split()))
    
    if not subset.issubset(a):
        is_superset = False
        break

print(is_superset)
