"""
p7
Write a function that takes an integer n and returns a random integer with exactly n digits. For
instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
that is really 93, which is a two-digit number.
"""
from random import randint
def digits(n):
    str_num = ''
    for i in range(n):
        x = randint(1,9)
        str_num += str(x)
    return int(str_num)


num = int(input("Enter the number of digits: "))
print(digits(num))