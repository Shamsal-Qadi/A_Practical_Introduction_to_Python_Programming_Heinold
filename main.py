"""
p5
Write a function called first_diff that is given two strings and returns the first location in
which the strings differ. If the strings are identical, it should return -1.
"""
def first_diff(string1 , string2):
    result = -1
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            result = i
            break
    return result

s1 ,s2 = input("Enter 2 strings: ").split()
print(first_diff(s1 , s2))