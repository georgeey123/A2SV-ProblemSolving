t = int(input())

for _ in range(t):
    n, k = map(int, input().split())  
    A = list(map(int, input().split()))
    cnt = [0] * 31 

    for x in A:
        for i in range(31):
            cnt[i] += (1 - ((x >> i) & 1))

    for i in range(30, -1, -1):
       
        if k >= cnt[i]:
            k -= cnt[i] 
            cnt[i] = 0

    ans = 0
    for i in range(0, 31):
        if cnt[i] == 0:
            ans += (1 << i)

    print(ans)
