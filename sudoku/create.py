from helpers import initial_matrix, full_swap, poke_hole
HOLES = 20

def main():
    matrix = initial_matrix()
    new_matrix = full_swap(matrix)

    for _ in range(HOLES):
        poke_hole(new_matrix)

    # for line in new_matrix:
    #     print(line)
    return new_matrix


if __name__ == '__main__':
    main()
