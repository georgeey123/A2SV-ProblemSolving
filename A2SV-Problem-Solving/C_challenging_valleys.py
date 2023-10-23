t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    rise = False
    found = True
 
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            rise = True
        if nums[i] < nums[i-1] and rise:
            found = False
 
    if found:
        print("YES")
    else:
        print("NO")
