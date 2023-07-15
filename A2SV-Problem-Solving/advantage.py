t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    values = sorted(nums)
 
    res = []
 
    for i in range(len(nums)):
        if nums[i] != values[-1]:
            res.append(nums[i] - values[-1])
        else:
            res.append(nums[i] - values[-2])
 
    print(*res)
