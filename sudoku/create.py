from helpers import initial_matrix, full_swap, poke_hole
import copy
HOLES = 30

def main():
    matrix = initial_matrix()
    new_matrix = full_swap(matrix)
    
    
    copy_matrix = copy.deepcopy(new_matrix)
    holed_matrix = poke_hole(copy_matrix, HOLES)

    # print('before matrix')
    # for line in new_matrix:
    #     print(line)
    

    

    # print('_' * 27)
    # for row in holed_matrix:
    #     print(row)
    return new_matrix, holed_matrix


if __name__ == '__main__':
    main()
