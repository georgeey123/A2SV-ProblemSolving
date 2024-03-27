#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    res = [0] * n
    
    for start, end, value in queries:
        if 0 <= start - 1 < n:
            res[start - 1] += value
             
        if 0 <= end < n:
            res[end] -= value
            
    max_sum = 0
    cur_sum = 0
        
    for i in res:
        cur_sum += i
        max_sum = max(max_sum, cur_sum)
    
    return max_sum
        # print(res)
    return max(res)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

#27/03/2024
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    res = [0] * n
    
    for start, end, value in queries:
        if 0 <= start - 1 < n:
            res[start - 1] += value
             
        if 0 <= end < n:
            res[end] -= value
            
    # max_sum = 0
    # cur_sum = 0
        
    for i in range(1, n):
        res[i] += res[i-1]
        # cur_sum += i
        # max_sum = max(max_sum, cur_sum)
    
    return max(res)
        # print(res)
    # return max(res)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

