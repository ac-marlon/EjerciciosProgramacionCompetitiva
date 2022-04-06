# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:52:03 2022

@author: Marlon
"""

# Problem description

"""

PROBLEM:

You are given a table with N rows and M columns. 
Each cell is colored with white or black. 
Considering the shapes created by black cells, what is the maximum border of 
these shapes? 
Border of a shape means the maximum number of consecutive black cells in any 
row or column without any white cell in between.

A shape is a set of connected cells. 
Two cells are connected if they share an edge. 
Note that no shape has a hole in it.

INPUT FORMAT:

The first line contains denoting the number of test cases.
The first line of each test case contains integers N, M denoting the number of 
rows and columns of the matrix. 
Here, '#' represents a black cell and '.' represents a white cell. 
Each of the next N lines contains M cells ('.' or '#').

OUTPUT FORMAT:

Print the maximum border of the shapes.

"""

# Maximum Border (own solution)

import re

test_cases = int(input())

while(test_cases > 0):
    longest_border = 0
    rows, cols = map(int, input().split())
    matrix = []

    for i in range(rows):
        row = input()
        matrix.append(list(row))
        len_row = len(max(re.findall('#+', row), default=''))

        if (longest_border < len_row):
            longest_border = len_row

    for j in range(cols):
        col = ''

        for i in range(rows):
            col = ''.join([col, matrix[i][j]])

        len_col = len(max(re.findall('#+', col), default=''))

        if (longest_border < len_col):
            longest_border = len_col

    print(longest_border)
    test_cases -= 1

# Test cases

"""

10
2 15
.....####......
.....#.........
7 9
...###...
...###...
..#......
.####....
..#......
...#####.
.........
18 11
.#########.
########...
.........#.
####.......
.....#####.
.....##....
....#####..
.....####..
..###......
......#....
....#####..
...####....
##.........
#####......
....#####..
....##.....
.#######...
.#.........
1 15
.....######....
5 11
..#####....
.#######...
......#....
....#####..
...#####...
8 13
.....######..
......##.....
########.....
...#.........
.............
#######......
..######.....
####.........
7 5
.....
..##.
###..
..##.
.....
..#..
.#...
14 2
..
#.
..
#.
..
#.
..
..
#.
..
..
..
#.
..
7 15
.###########...
##############.
...####........
...##########..
.......#.......
.....#########.
.#######.......
12 6
#####.
###...
#.....
##....
###...
......
.##...
..##..
...#..
..#...
#####.
####..

"""