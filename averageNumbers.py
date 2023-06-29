n = int(input())
nums = list(map(int, input().split()))

total_sum = sum(nums)
indices = []

for i in range(n):
    sum_exc_i = total_sum - nums[i]
    mean = sum_exc_i / (n-1)
    if nums[i] == mean:
        indices.append(i+1)

print(len(indices))
print(*indices)
