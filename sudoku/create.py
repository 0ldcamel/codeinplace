from helpers import initial_matrix, check_boxes, check_box, check_row, check_column

matrix = initial_matrix()
print('Before')
print(check_boxes(matrix))

# swap 2 numbers
# matrix[3][7], matrix[7][3] =  5, 5
# matrix[2][7], matrix[7][2] =  6, 6
print(check_box(1, 1, matrix))
