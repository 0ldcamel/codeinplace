import create 
from helpers import print_matrix

def main():
    matrix = create.main()
    print_matrix(matrix)
    print('_' * 27, '\n')
    for _ in range(500):
        single_cand(matrix)
    print_matrix(matrix)

def check_zero(matrix):
    for row in matrix:
        if 0 in row:
            return True
    return False

def single_cand(matrix):
    for i in range(9):
        for j in range(9):
            if len(pos_avail(j, i, matrix)) == 1 and matrix[j][i] == 0:
                # print(f'SC: row {j}, column {i}, is updated to {pos_avail(j, i, matrix)[0]}')
                matrix[j][i] = pos_avail(j, i, matrix)[0]

def box_candidates(row, column, matrix):
    top_row = row // 3
    left_col = column // 3
    numbers = list(range(1, 10))
    for i in range(3):
        for j in range(3):
            number = matrix[3 * top_row + j][3 * left_col + i]
            if number in numbers:
                numbers.remove(number)
    return numbers

def pos_avail(row, column, matrix):
    row_avail = row_candidates(row, matrix)
    col_avail = column_candidates(column, matrix)
    box_avail = box_candidates(row, column, matrix)
    common = []
    row_col = []
    for number in row_avail:
        if number in col_avail:
            row_col.append(number)
    for number in row_col:
        if number in box_avail:
            common.append(number)
    return common

def row_candidates(row, matrix):
    row_list = matrix[row]
    numbers = list(range(1, 10))
    for number in row_list:
        if number in numbers:
            numbers.remove(number)
    return numbers

def column_candidates(column, matrix):
    numbers = list(range(1, 10))
    for i in range(9):
        number = matrix[i][column]
        if number in numbers:
            numbers.remove(number)
    return numbers

if __name__ == '__main__':
    main()