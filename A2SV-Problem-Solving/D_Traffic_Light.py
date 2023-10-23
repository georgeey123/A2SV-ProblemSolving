t = int(input())

for v in range(t):
    n, c = map(str, input().split())
    s = list(input())
    n = int(n)
    s += s
    
    count = 0
    maxx = 0
    flag = False
    
    for i in range(len(s)):
        if s[i] == c:
            flag = True
        if s[i] == 'g':
            flag = False
            maxx = max(maxx, count)
            count = 0
        if flag:
            count += 1
            
    print(maxx)
