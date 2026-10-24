"""
p10
Write a function called closest that takes a list of numbers L and a number n and returns
the largest element in L that is not larger than n . For instance, if L=[1,6,3,9,11] and n=8 ,
then the function should return 6, because 6 is the closest thing in L to 8 that is not larger than
8. Don’t worry about if all of the things in L are smaller than n
"""

def closest(l , n):
    l.sort()
    x = 0
    for i in range(len(l) -1):
        if l[i] > n:
            x = l[i - 1]
    return x

lis = [int(i) for i in input().split()]
highest = int(input())
print(closest(lis , highest))