#!/bin/python3

import math
import os
import random
import re
import sys


def inside(n, m, x, y):
    return x >= 0 and y >= 0 and x < n and y < m


def solve(n, m, grid, i, j):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    val = grid[i][j]
    
    for k in range(8):
        ndx = i + dx[k]
        ndy = j + dy[k]
        if inside(n, m, ndx, ndy):
            if val <= grid[ndx][ndy]:
                return 0
    return 1


def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += solve(n, m, grid, i, j)
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
