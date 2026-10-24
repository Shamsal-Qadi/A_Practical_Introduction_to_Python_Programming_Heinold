"""
p3
Write a function called sum_digits that is given an integer num and returns the sum of the
digits of num .
"""
def sum_digits(num):
    num = str(num)
    ans = 0
    for i in num:
        ans += int(i)
    return ans

n = int(input("Enter the number: "))
print(sum_digits(n))