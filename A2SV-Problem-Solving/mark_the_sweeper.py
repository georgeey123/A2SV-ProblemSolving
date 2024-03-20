t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = 0

    for i in range(n-1):
        if arr[i+1] == 0 and arr[i] != 0:
            arr[i] -= 1
            arr[i+1] += 1
            res += 1

    for i in range(n-1):
        res += arr[i]
    print(res)
