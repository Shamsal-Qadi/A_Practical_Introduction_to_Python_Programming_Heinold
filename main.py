"""
p2
(a) Write a function called add_excitement that takes a list of strings and adds an excla-
mation point ( ! ) to the end of each string in the list. The program should modify the
original list and not return anything.
(b) Write the same function except that it should not modify the original list and should
instead return a new list.
"""
def add_excitement(list_string):
    for i in range(len(list_string)):
        list_string[i] += '!'
        print(list_string[i],end=' ')




s = input("Enter the string: ").split()
add_excitement(s)
print(s)


def add_excitement(list_string):
    new = []
    for item in list_string:
        new.append(item + '!')
    return new

s = input("Enter the string: ").split()
print(add_excitement(s))
print(s)
