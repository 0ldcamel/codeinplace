from helpers import column_to_list, print_matrix
import create

def main():
    matrix = [
        [5, 4, 0, 9, 0, 7, 2, 0, 1],
        [0, 0, 3, 0, 5, 4, 0, 0, 7],
        [8, 7, 0, 0, 0, 0, 0, 0, 4],
        [4, 6, 5, 8, 0, 9, 0, 2, 3],
        [7, 9, 0, 2, 1, 3, 0, 5, 6],
        [1, 3, 0, 5, 0, 6, 7, 8, 9],
        [6, 0, 0, 0, 0, 0, 0, 1, 2],
        [3, 0, 0, 4, 6, 0, 9, 0, 0],
        [9, 0, 7, 1, 0, 2, 0, 4, 5],
    ]
    print_matrix(matrix)
    print('_' * 27, '\n')
    single_pos(matrix)

def single_pos(matrix):
    for value in range(1, 10):
        for row in range(9):
            columns = pos_in_row(value, row, matrix) # return list of columns
            positions = check_row_col(value, row, columns, matrix)
            if len(positions) == 1:
                row = positions[0][0]
                col = positions[0][1]
                n = pos_in_box(value, row, col, matrix)
                if n:
                    # print(f'SP, row {row}, col {col} is updated to {value}.')
                    matrix[row][col] = value

    return matrix

def check_row_col(value, row, columns, matrix):
    positions = []
    for col in columns:
        pos = pos_in_col(value, row, col, matrix)
        if len(pos) > 0:
            positions.append([row, col])
    # print(positions)
    return positions

def row_col_list():
    pos = []
    for i in range(9):
        for j in range(9):
            pos.append([i, j])
    return pos

def pos_in_row(value, row, matrix):
    # find possible position in row
    indexes = []
    row_list = matrix[row]
    if value in row_list:
        return indexes
    for i in range(9):
        if row_list[i] == 0:
            indexes.append(i)
    return indexes

def pos_in_col(value, row, col, matrix):
    # find possible position in column
    indexes = []
    col_list = column_to_list(col, matrix)
    if value in col_list:
        return indexes
    elif col_list[row] == 0:
        indexes.append(col_list[row])
    return indexes   

def pos_in_box(value, row, col, matrix):
    top_row = row // 3
    left_col = col // 3
    box_list = box_to_list(top_row * 3, left_col * 3, matrix)
    # print('box_list', box_list)
    if value in box_list:
        return False
    return True

def box_to_list(top_row, left_col, matrix):
    lst = []
    for i in range(3):
        for j in range(3):
            lst.append(matrix[i + top_row][j + left_col])
    return lst

if __name__ == '__main__':
    main()
