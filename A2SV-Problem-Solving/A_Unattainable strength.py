def solve(n, artifacts):
  artifacts.sort()
  cur_sum = 0
  
  for artifact in artifacts:
    if artifact > cur_sum + 1:
      return cur_sum + 1
    cur_sum += artifact
  return cur_sum + 1
  
 
n = int(input())
artifacts = list(map(int, input().split()))
result = solve(n, artifacts)
print(result)
