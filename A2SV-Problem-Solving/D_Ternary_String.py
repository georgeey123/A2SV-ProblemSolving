t = int(input())

for i in range(t):
    s = input()
    n = len(s)

    count = {1: 0, 2: 0, 3: 0}
    left = right = 0
    min_length = float('inf')

    while right < n:
        count[int(s[right])] += 1

        while all(count.values()):
            min_length = min(min_length, right - left + 1)
            count[int(s[left])] -= 1
            left += 1

        right += 1

    if min_length == float('inf'):
        print(0)
    else:
        print(min_length)
