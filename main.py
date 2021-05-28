import os
from solver import solve_quadratic

answer = solve_quadratic(5, 6, 1)
print(answer)

my_secret = os.environ['top']
print(my_secret)