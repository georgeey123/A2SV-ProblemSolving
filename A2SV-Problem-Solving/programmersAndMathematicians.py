t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    l, r = 0, (a+b)//4
    ans = 0
    
    while l <= r:
        mid = l + (r-l) // 2
        
        if (a+b)//4 >= mid and a >= mid and b >= mid:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
            
    print(ans)
  
#first approach: NAIVE
t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    
    max_teams = min(a, b, (a+b)//4)
    
    print(max_teams)
