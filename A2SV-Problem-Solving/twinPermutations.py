t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []

    for num in arr:
        res.append(n-num+1)

    print(*res)
