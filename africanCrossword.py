from collections import Counter

n, m = map(int, input().split())

grid = []

for i in range(n):
    row = input()
    grid.append(row)

duplicate_array = grid.copy()

word = ""

for i in range(n):
    row = grid[i]
    count = Counter(row)
    for j in range(m):
        if count[row[j]] > 1:
            duplicate_array[i] = duplicate_array[i][:j] + "#" + duplicate_array[i][j+1:]

for j in range(m):
    col = [grid[i][j] for i in range(n)]
    count = Counter(col)
    for i in range(n):
        if count[col[i]] > 1:
            duplicate_array[i] = duplicate_array[i][:j] + "#" + duplicate_array[i][j+1:]


for i in range(n):
    for j in range(m):
        if duplicate_array[i][j] != "#":
            word += duplicate_array[i][j]

print(word)
