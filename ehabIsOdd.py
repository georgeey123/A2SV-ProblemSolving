n = int(input())

arr = list(map(int, input().split()))

even_count, odd_count = 0,0

for i in range(n):
    if arr[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > 0 and odd_count > 0:
    arr.sort()

print(*arr)
