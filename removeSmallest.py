t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    for i in range(n-1):
        if abs(a[i+1] - a[i]) > 1:
            print("NO")
            break
    else:
        print("YES")
