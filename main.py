import os
from solver import solve_quadratic

answer = solve_quadratic(5, 6, 1)
print(answer)

my_secret = os.environ['top']
print(my_secret)

# Print comprehensive list
c_list=[x * 2 for x in range(5)]
print(c_list)