import math

for i in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = 0
    for j in range(n):
        if (p[j] - j - 1) % k != 0:
            c += 1
    c = math.ceil(c / 2)
    
    if c == 0:
        print(0)
    elif c == 1:
        print(1)
    else:
        print(-1)
