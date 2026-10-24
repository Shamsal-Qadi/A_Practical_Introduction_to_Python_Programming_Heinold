"""
p9
Write a function called factors that takes an integer and returns a list of its factors.
"""
def factors(n):
    l = []
    for i in range(1, n +1):
        if n % i == 0:
            l.append(i)
    return l

num = int(input("Enter the number: "))
print(factors(num))