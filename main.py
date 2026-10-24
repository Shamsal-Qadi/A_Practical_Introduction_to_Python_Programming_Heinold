"""
p6
Write a function
called binom that takes two integers n and k and returns the binomial coefficient
(nk) . The definition is nk = n! / k!(n−k)!
Numerator and denominator .
"""

def binom(n , k):
    num, denom, de_new = 1, 1, 1
    for i in range(n,0,-1):
        num *= i
    for i in range(k,0,-1):
        denom *= i
    new = n - k
    for i in range(new,0,-1):
        de_new *= i
    denom *= de_new
    return num / denom

a , b = input("Enter tow numbers: ").split()
a , b = int(a) , int(b)
print(binom(a , b))