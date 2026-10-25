# """
# p20
# Write a function called merge that takes two already sorted lists of possibly different lengths,
# and merges them into a single sorted list.
# (a) Do this using the sort method.
# (b) Do this without using the sort method.
# """
# def merge(list1 , list2):            #l1 : [5, 8, 9]        l2: [2, 6, 8]
#     new_l = list1 + list2            #new_l : [5, 8, 9, 2, 6, 8]
#     l = []
#
#     for i in range(len(new_l) -2):
#         if new_l[i] > new_l[i +1]:
#             new_l[i] , new_l[i +1] = new_l[i +1] , new_l[i]
#     return new_l
#
# l1 = input().split()
# l2 = input().split()
# print(merge(l1 , l2))

"""
p21
In Chapter 12, the way we checked to see if a word w was a real word was:
if w in words:
where words was the list of words generated from a wordlist. This is unfortunately slow, but
there is a faster way, called a binary search. To implement a binary search in a function, start
by comparing w with the middle entry in words . If they are equal, then you are done and
the function should return True . On the other hand, if w comes before the middle entry, then
search the first half of the list. If it comes after the middle entry, then search the second half of
the list. Then repeat the process on the appropriate half of the list and continue until the word
is found or there is nothing left to search, in which case the function short return False . The
< and > operators can be used to alphabetically compare two strings.
"""
def binary_search(li , w):
    #l: ["asd", "cvb", "ert", "opj", "qwe"]
    #w: "opj"
    l , r = 0 , len(li) - 1
    while l <= r :
        mid = (r + l) // 2
        if li[mid] == w :
            return  True
        elif li[mid] < w :
            l = mid + 1
        else:
            r = mid - 1
    return False
words = input("Enter list of words: ").split()
words.sort()
s = input("Enter the specific word: ")
print(binary_search(words , s))