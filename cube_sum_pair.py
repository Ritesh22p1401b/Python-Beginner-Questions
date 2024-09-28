import math

def cube_sum(n):
    x = int(math.pow(n, 1 / 3) + 1)
    count = 0
    for i in range(1, x):
        cube = i * i * i
        diff = n - cube
        cube_diff = int(math.pow(diff, 1 / 3))
        if cube_diff*cube_diff*cube_diff == diff:
            count += 1
    print(count)


n = int(input())
cube_sum(n)
