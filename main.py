"""
p20
Write a function called merge that takes two already sorted lists of possibly different lengths,
and merges them into a single sorted list.
(a) Do this using the sort method.
(b) Do this without using the sort method.
"""
def merge(list1 , list2):
    new_l = list1 + list2
    new_l.sort()
    return new_l

l1 = input().split()
l2 = input().split()
print(merge(l1 , l2))