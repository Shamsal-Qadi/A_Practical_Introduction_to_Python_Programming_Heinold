"""
p11
Write a function called matches that takes two strings as arguments and returns how many
matches there are between the strings. A match is where the two strings have the same character
at the same index. For instance, 'python' and 'path' match in the first, third, and
fourth characters, so the function should return 3.
"""

def matches(string1 , string2):
    c = 0
    if len(string1) > len(string2):
        string1 , string2 = string2 , string1
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            c += 1
    return c

s1, s2 = input().split()
print(matches(s1 , s2))