from helpers import box_to_list
import create

matrix = create.main()
print('Print Matrix')
for row in matrix:
    print(row)

lst = box_to_list(6, 6, matrix)
print('Print List')
print(lst)
