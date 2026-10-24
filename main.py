"""
p15
Write a function called root that is given a number x and an integer n and returns x 1/n . In
the function definition, set the default value of n to 2.
"""

def root(x , n=2):
    ans = x**(1/n)
    return ans

a , b = [int(i) for i in input().split()]
print(root(a , b))