#!/usr/bin/python3
"""0-island_perimeter.py"""


def island_perimeter(grid):
    """calculate perimeter of island"""
    height = len(grid)
    if height == 0:
        return 0

    width = len(grid[0])
    if height == 0:
        return 0

    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:

                adjacent_ones = 0

                if i > 0 and grid[i - 1][j] == 1:
                    adjacent_ones += 1
                if i < height - 1 and grid[i + 1][j] == 1:
                    adjacent_ones += 1
                if j < width - 1 and grid[i][j + 1] == 1:
                    adjacent_ones += 1
                if j > 0 and grid[i][j - 1] == 1:
                    adjacent_ones += 1

                perimeter += 4 - adjacent_ones

    return perimeter
