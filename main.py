"""
p30
Pascal’s triangle is shown below. On the outside are 1’s and each other number is the sum of
the two numbers directly above it. Write a program to generate Pascal’s triangle. Allow the
user to specify the number of rows. Be sure that it is nicely formatted, like below.
"""

print(5*' ',1,5*' ',sep='')
i = 4
j = 1
while i != 0:
    print(i*' ',1,j*' ',1,i*' ',sep='')
    j += 2
    i -= 1