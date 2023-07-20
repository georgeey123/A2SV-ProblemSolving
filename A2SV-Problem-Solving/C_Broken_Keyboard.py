t=int(input())

for i in range(t):
    s = input()
    s_sorted = sorted(set(s))
    res=''
    for j in s_sorted:
        if s.count(j) > 2 * s.count(j+j):
            res=res+j
    print(res)
                                          