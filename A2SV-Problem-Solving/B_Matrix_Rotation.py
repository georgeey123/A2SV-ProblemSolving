'''
idea:
check if the matrix is beautiful. if not, rotate and check again. 
counter variable should be initialisjed to keep track of number of operations.

rotate algorithm:
initiaise top left, top right, bottom left and bottom right pointers. 
check of left < right
if not, create temp variable and assign to bottom right pointer, 
set top right to bottom right, top left to top right, bottom left to top left 
then temp to bottom left.
'''

def is_beautiful_matrix(matrix):
    row1 = matrix[0]
    row2 = matrix[1]

    if row1[0] < row1[1] and row2[0] < row2[1]:
        col1 = [row1[0], row2[0]]
        col2 = [row1[1], row2[1]]

        if col1[0] < col1[1] and col2[0] < col2[1]:
            return True

    return False


def rotate_matrix(matrix):
    return [[matrix[1][0], matrix[0][0]], [matrix[1][1], matrix[0][1]]]


t = int(input())
test_cases = []

for i in range(t):
    matrix = []
    for j in range(2):
        row = list(map(int, input().split()))
        matrix.append(row)
    test_cases.append(matrix)

for matrix in test_cases:
    if is_beautiful_matrix(matrix):
        print("YES")
    else:
        rotated_matrix = rotate_matrix(matrix)
        rotations = 1

        while not is_beautiful_matrix(rotated_matrix) and rotations < 4:
            rotated_matrix = rotate_matrix(rotated_matrix)
            rotations += 1

        if is_beautiful_matrix(rotated_matrix):
            print("YES")
        else:
            print("NO")
