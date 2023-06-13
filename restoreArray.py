def solve():
    n = int(input())
    v = list(map(int, input().split()))

    print(v[0], end=" ")
    for i in range(n - 2):
        print(min(v[i], v[i + 1]), end=" ")
    print(v[n - 2])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
