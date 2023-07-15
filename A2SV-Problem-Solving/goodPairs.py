t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    min_index = nums.index(min(nums)) + 1
    max_index = nums.index(max(nums)) + 1
 
    print(min(min_index, max_index), max(min_index, max_index))
