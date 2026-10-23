from random import randint
"""
p29
The following is useful as part of a program to play Minesweeper. Suppose you have a 5 × 5
list that consists of zeros and M’s. Write a program that creates a new 5 × 5 list that has M’s in
the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells
(adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint:
short-circuiting may be helpful for avoiding index-out-of-range errors.]
0 m 0 m 0
0 0 m 0 0
0 0 0 0 0
m m 0 0 0
0 0 0 m 0
"""
l = [[randint(0,1) for i in range(5)] for j in range(5)]

for row in l :
    for i in range(len(row)):
        if row[i] == 1:
            row[i] = 'm'

for row in l :
    print(row)


for i in range(5) :
    for j in range(5):
        if l[i][j] == 0:
            if 0 <= (i - 1) <= 4 and l[i - 1][j] == 'm':
                l[i][j] += 1
            if 0 <= (i + 1) <= 4 and l[i + 1][j] == 'm':
                l[i][j] += 1
            if 0<= (j + 1) <= 4 and l[i][j + 1] == 'm':
                l[i][j] += 1
            if 0<= (j - 1) <= 4 and l[i][j - 1] == 'm':
                l[i][j] += 1
            if 0 <= (i - 1) <= 4 and 0<= (j - 1) <= 4 and l[i - 1][j - 1] == 'm':
                l[i][j] += 1
            if 0 <= (i - 1) <= 4 and 0<= (j + 1) <= 4 and l[i - 1][j + 1] == 'm':
                l[i][j] += 1
            if 0 <= (i + 1) <= 4 and 0<= (j - 1) <= 4 and l[i + 1][j - 1] == 'm':
                l[i][j] += 1
            if 0 <= (i + 1) <= 4 and 0<= (j + 1) <= 4 and l[i + 1][j + 1] == 'm':
                l[i][j] += 1




for row in l :
    print(row)