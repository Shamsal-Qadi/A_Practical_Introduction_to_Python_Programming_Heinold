"""
p13
Write a function called change_case that given a string, returns a string with each upper
case letter replaced by a lower case letter and vice-versa.
"""

def change_case(string):
    string = string.lower()
    return string[-1::-1]

s = input()
print(change_case(s))