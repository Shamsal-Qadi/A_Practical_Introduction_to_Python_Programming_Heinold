"""
p14
Write a function called is_sorted that is given a list and returns True if the list is sorted
and False otherwise.
"""

def is_sorted(l):
    copy = l[:]
    copy.sort()
    if l == copy:
        return True
    else:
        return False

L = input().split()
print(is_sorted(L))