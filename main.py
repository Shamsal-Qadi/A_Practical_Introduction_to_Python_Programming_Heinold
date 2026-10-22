"""
p25
Write a program that finds all integer solutions to Pell’s equation x^2 − 2y^2 = 1 , where x and
y are between 1 and 100.
"""

for i in range(1,100 +1):
    for j in range(1,100 +1):
        if i**2 - 2*(j**2) == 1:
            print(i,j)