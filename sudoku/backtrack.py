board = [
    [6, 0, 1, 3, 0, 4, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 5],
    [7, 0, 0, 0, 8, 2, 6, 0, 0],
    [0, 0, 7, 0, 0, 0, 3, 8, 0],
    [0, 0, 0, 0, 3, 1, 0, 5, 7],
    [2, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 7, 6, 1, 2, 9, 4, 3, 0],
    [0, 8, 9, 7, 0, 3, 5, 6, 2],
    [0, 4, 2, 0, 0, 0, 0, 0, 1]

]

def is_valid(board, number, position):
    row = position[0]
    column = position[1]
    # check row
    if number in board[row]:
        return False
    # check column
    for i in range(9):
        if board[i][column] == number:
            return False
    # check box
    top_row = row // 3
    left_column = column // 3
    for i in range(3):
        for j in range(3):
            if board[top_row * 3 + i][left_column * 3 + j] == number:
                return False
    return True

def find_empty(board):
    empties = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empties.append((i, j))
    return empties

def single_value(board, position):
    values = []
    for i in range(1, 10):
        if is_valid(board, i, position):
            values.append(i)
    if len(values) == 1:
        board[position[0]][position[1]] = values[0]
        print("Update by single value", position, values[0])
        
def solve_single_value(board):
    for _ in range(20):
        empties = find_empty(board)
        print(empties)
        for position in empties:
            single_value(board, position)

    
def solve(board):
    solve_single_value(board)
    empties = find_empty(board)
    for position in empties:
        for i in range(1, 10):
            if is_valid(board, i, position):
                board[position[0]][position[1]] = i
                print("Update by solve", position, i)
                solve(board)
            
    solve_single_value(board)


solve(board)

for row in board:
    print(row)