import random

SWAP = 100

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
            value = matrix[i + top_row][j + left_col]
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
    for i in range(3):
        for j in range(3):
            top_row = i * 3
            left_column = j * 3
            if not check_box(top_row, left_column, matrix):
                return False
    return True
        
def swap_what(matrix, index):
    swaps = ['row', 'column']
    swap = random.choice(swaps)
    if swap == 'row':
        return swapping_rows(matrix, index)
    else:
        return swapping_columns(matrix, index)

def get_other(index):
    indexes = [0, 1, 2]
    base_index = index // 3
    local_index = index - base_index * 3
    indexes.remove(local_index)
    other_index = random.choice(indexes)
    return other_index + base_index * 3

def swapping_columns(matrix, index):
    other_index = get_other(index)
    # print(f'swap column {other_index} with column {index}')
    for i in range(9):
        matrix[i][index], matrix[i][other_index] = matrix[i][other_index], matrix[i][index]
    return matrix    

def swapping_rows(matrix, index):
    other_index = get_other(index)
    # print(f'swap row {other_index} with row {index}')
    for i in range(9):
        matrix[index][i], matrix[other_index][i] = matrix[other_index][i], matrix[index][i]
    return matrix

def full_swap(matrix):
    indexes = list(range(9))
    for i in range(SWAP): # how many swap?
        index = random.choice(indexes)
        swap_what(matrix, index)
    return matrix