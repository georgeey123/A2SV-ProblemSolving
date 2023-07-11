n_col = int(input())

n_cubes = list(map(int, input().split()))

flip = sorted(n_cubes)

print(*flip)
