n, k = map(int, input().split())

sequence = list(map(int, input().split()))

sequence.sort()


if k == 0 and sequence[0] > 1:
    print(1)
elif k == 0 and sequence[0] == 1:
    print(-1)
elif k <= n - 1:
    if sequence[k - 1] != sequence[k]:
        print(sequence[k - 1])
    else:
        print(-1)
elif k == n:
    print(sequence[k - 1])
