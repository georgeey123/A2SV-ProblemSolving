from collections import defaultdict

n,m = map(int, input().split())

indicies = defaultdict(list)

for i in range(1, n+1):
    word = input()
    indicies[word].append(i)
    
for i in range(1, m+1):
    word = input()
    if word in indicies:
        print(*indicies[word])
    else:
        print(-1)
