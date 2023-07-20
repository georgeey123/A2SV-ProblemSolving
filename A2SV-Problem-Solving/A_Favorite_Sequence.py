'''
idea:

initialise 2 pointers. one at the beginning, one at the end. 
go through the array, if the index of the element is even, keep it 
and increase left by 1, if it is odd, swap with right pointer and decrease pointer
'''
t = int(input())

for _ in range(t):
    seq_len = int(input())

    sequence = list(map(int, input().split()))

    result = []
    left, right = 0, seq_len - 1

    for i in range(seq_len):
        if i % 2 == 0:
            result.append(sequence[left])
            left += 1
        else:
            result.append(sequence[right])
            right -= 1

    print(*result)
