from helpers import initial_matrix, check_boxes

matrix = initial_matrix()
print('Before')
print(check_boxes(matrix))

# swap 2 numbers
matrix[3][7], matrix[7][3] =  matrix[7][3], matrix[3][7]
matrix[2][7], matrix[7][2] =  matrix[7][2], matrix[2][7]
print('After')
print(check_boxes(matrix))

