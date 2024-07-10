import create
from single_candidate import single_cand, check_zero, pos_avail
from single_post import single_pos
from helpers import print_matrix

# matrix = create.main()
def main():
    matrix, holed_matrix = create.main()
    print_matrix(matrix)
    print('-' * 27)
    """matrix =    [
            [3, 2, 1, 5, 4, 6, 0, 9, 0],
            [6, 5, 4, 8, 7, 9, 2, 3, 1],
            [9, 8, 7, 2, 1, 3, 5, 6, 4],
            [2, 1, 3, 4, 6, 5, 0, 0, 9],
            [5, 4, 6, 7, 9, 8, 1, 2, 3],
            [8, 7, 9, 1, 3, 2, 4, 5, 6],
            [1, 3, 2, 6, 5, 4, 9, 0, 0],
            [4, 6, 5, 9, 8, 7, 3, 1, 2],
            [7, 9, 8, 3, 2, 1, 6, 4, 5]
            ]"""
    new_matrix = singles(holed_matrix)
    print_matrix(holed_matrix)
    if holed_matrix == matrix:
        print("True")
    else:
        print("False")


def singles(matrix):
    for i in range(1000):
        # print(i)
        single_cand(matrix)
        single_pos(matrix)
        i += 1
        if not check_zero(matrix):
            # print(f'solved after {i} steps, {not check_zero(matrix)}')
            return matrix

    if check_zero(matrix):
        # print("Not solved")
        for i in range(100):
            copy_matrix = try_n_error(matrix)
            single_cand(copy_matrix)
            single_pos(copy_matrix)
            if not check_zero(copy_matrix):
                return copy_matrix
            # else:
            #     print('Not solved even with try and error')



def try_n_error(matrix):
    copy_matrix = matrix.copy()
    row_index = find_zero(copy_matrix)
    values, col_index = find_value(row_index, copy_matrix)
    copy_matrix[row_index][col_index] = values[0]
    return copy_matrix

    

def find_zero(matrix):
    for i in range(9):
        row = matrix[i]
        if 0 in row:
            return i
    
def find_value(i, matrix):
    full_list = list(range(1, 10))
    n = matrix[i].index(0)
    for value in matrix[i]:
        
        if value != 0:
            full_list.remove(value)
    return full_list, n




if __name__ == '__main__':
    main()

