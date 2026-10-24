"""
p1
Write a function called rectangle that takes two integers m and n as arguments and prints
out an m × n box consisting of asterisks. Shown below is the output of rectangle(2,4)
****
****
"""
def rectangle(m , n):
    for i in range(m):
        for j in range(n):
            print('*',end='')
        print()

a , b = [int(i) for i in input().split()]
rectangle(a ,b)