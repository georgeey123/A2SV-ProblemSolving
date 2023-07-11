t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    a.sort()
    b.sort()
    ans = "YES"
    for i in range(n):
        if a[i] != b[i] and a[i] + 1 != b[i]:
            ans = "NO"
            break
            
    print(ans)
