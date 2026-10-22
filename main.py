"""
23,24 ???
Write a program that asks the user for a number and prints out all the ways to write the
number as difference of two perfect squares, x^2 − y^2 , where x and y are both between 1 and
1000. Writing a number as a difference of two squares leads to clever techniques for factoring
large numbers.
"""
num = int(input("enter the number: "))
for i in range(1,1000 +1):
    x = i
    y = num - i
    if x**2 - y**2 == 0:
        print(x,y)