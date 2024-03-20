t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    res = 0
    fill = False

    for i in range(n):
        if s[i] == '.':
            res += 1
        if i <= n - 3:
            if s[i] == '.' and s[i + 1] == '.' and s[i + 2] == '.':
                fill = True

    if fill:
        print("2")
    else:
        print(res)
