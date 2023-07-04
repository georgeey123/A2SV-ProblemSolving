t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for j in range(1, n):
        if arr[j - 1] > arr[j]:
            ans += 1

    if ans != n - 1:
        print("YES")
    else:
        print("NO")
