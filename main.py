"""
p16
Write a function called one_away that takes two strings and returns True if the strings are of
the same length and differ in exactly one letter, like bike/hike or water/wafer .
"""

def one_way(string1 , string2):
    if len(string1) == len(string2):
        c = 0
        for i in range(len(string2)):
            if string1[i] != string2[i]:
                c += 1
        if c == 1:
            return True
        else:
            return False
    else:
        return False


s1 ,s2 = input("Enter 2 strings: ").split()
print(one_way(s1 , s2))