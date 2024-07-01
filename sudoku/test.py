import create
from single_candidate import single_cand, check_zero, pos_avail
from single_post import single_pos
from helpers import print_matrix

matrix = create.main()

for i in range(1000):
    single_cand(matrix)
    single_pos(matrix)
    if not check_zero(matrix):
        print(f'solved after {i} steps, {not check_zero(matrix)}')
        break
if check_zero(matrix):
    print("Not solved")
print_matrix(matrix)

