def solve():
    n = int(input())
    sign = 1
    res = 0
    total_sum = 0
 
    a = list(map(int, input().split()))
 
    for num in a:
        total_sum += abs(num)
        if num < 0 and sign == 1:
            res += 1
            sign = -1
        elif num > 0:
            sign = 1
 
    print(total_sum, res)
 
 
t = int(input())
for _ in range(t):
    solve()
