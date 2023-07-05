t = int(input())
 
for i in range(t):
    n = int(input())
    robots = list(map(int, input().split()))
    
    max_robot = max(robots)
    robots_count = [0] * (max_robot + 1)
    
    for num in robots:
        robots_count[num] += 1
        
    for i in range(len(robots_count) - 1):
        if robots_count[i] < robots_count[i+1]:
            print("NO")
            break
    else:
        print("YES")
