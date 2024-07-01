
def single_can(i, j, matrix):
    possibility = []
    if matrix[i][j] != 0:
        pass
    else:
        for i in range(1, 10):
            pass

def get_col_values(col, matrix):
    col_val = []
    for i in range(9):
        if matrix[i][col] != 0:
            col_val.append(matrix[i][col])
    return col_val

def get_box_values(row, col, matrix):
    top_row = row // 3
    left_col = col // 3
    box_val = []
    for i in range(3):
        for j in range(3):
            if matrix[i + top_row * 3][j + left_col * 3] != 0:
                box_val.append(matrix[i + top_row * 3][j + left_col * 3])
    return box_val



