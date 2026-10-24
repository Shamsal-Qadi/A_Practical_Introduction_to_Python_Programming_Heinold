"""
p8
Write a function called number_of_factors that takes an integer and returns how many
factors the number has.
"""
def number_of_factors(n):
    c = 0
    for i in range(1, n +1):
        if n%i == 0:
            c += 1
    return c

num = int(input("Enter the number: "))
print(number_of_factors(num))