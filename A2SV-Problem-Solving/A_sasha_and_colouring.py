t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    cost = 0

    for i in range(n//2):
        cost += (a[n-1-i] - a[i])
    print(cost)
