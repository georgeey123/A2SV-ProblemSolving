t = int(input()) 
 
for _ in range(t):
    input()
 
    board = [input() for _ in range(8)]
 

    for row in range(1, 7):
        for col in range(1, 7):
            if (board[row][col] == '#' and board[row-1][col-1] == '#' 
            and board[row-1][col+1] == '#' and board[row+1][col-1] == '#' 
            and board[row+1][col+1] == '#'):
                print(row + 1, col + 1)
                break
        else:
            continue
        break
