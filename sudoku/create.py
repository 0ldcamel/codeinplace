from helpers import initial_matrix, check_boxes, full_swap

def main():
    matrix = initial_matrix()
    new_matrix = full_swap(matrix)
    print(check_boxes(new_matrix))
    for row in new_matrix:
        print(row)


if __name__ == '__main__':
    main()
