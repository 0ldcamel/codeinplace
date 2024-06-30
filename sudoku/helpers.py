import random

def initial_matrix():
    lists = make_list()
    i_matrix = []
    for list in lists:
        i_matrix += (three_rows(list))
    return i_matrix

def make_list():
    nuclear_1 = list(range(1, 10))
    base_list_1 = nuclear_1 + nuclear_1
    base_list_2 = mod_list(base_list_1)
    base_list_3 = mod_list(base_list_2)
    return base_list_1, base_list_2, base_list_3

def three_rows(base_list):
    matrix_out = [] # create top 3 lines
    for i in range(3):
        row = []
        offset = i * 3
        for j in range(9):
            row.append(base_list[j + offset])
        matrix_out.append(row)
    return matrix_out

def mod_list(list_in):
    list_out = list_in.copy()
    for j in range(6):
        i = j * 3
        list_out[i], list_out[i + 1], list_out[i + 2] = list_out[i + 2], list_out[i], list_out[i + 1] 
    return list_out

def check_row(row, matrix):
    check_set = set()
    for i in range(9):
        value = matrix[row][i]
        check_set.add(value)
    if len(check_set) == 9:
        return True
    return False

def check_box(top_row, left_col, matrix):
    check_set = set()
    for i in range(3):
        for j in range(3):
            value = matrix[i][j]
            check_set.add(value)
    if len(check_set) == 9:
        return True
    return False


def check_column(col, matrix):
    check_set = set()
    for i in range(9):
        value = matrix[i][col]
        check_set.add(value)
    if len(check_set) == 9:
        return True
    return False

def check_boxes(matrix):
    values = []
    for i in range(3):
        for j in range(3):
            if check_box(i, j, matrix):
                continue
            else:
                return False
    return True
    
            

matrix = initial_matrix()
print(check_boxes(matrix))

