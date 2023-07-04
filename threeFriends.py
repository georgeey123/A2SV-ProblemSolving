t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    a.sort()

    if a[0] == a[1] and a[1] == a[2]:
        ans = 0
    elif a[0] == a[1]:
        a[0] += 1
        a[1] += 1
        if a[2] != a[1]:
            a[2] -= 1
        ans = abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[0] - a[2])
    elif a[1] == a[2]:
        a[1] -= 1
        a[2] -= 1
        if a[0] != a[1]:
            a[0] += 1
        ans = abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[0] - a[2])
    else:
        a[0] += 1
        a[2] -= 1
        ans = abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[0] - a[2])

    print(ans)
