"""
p17
(a) Write a function called primes that is given a number n and returns a list of the first n
primes. Let the default value of n be 100.
(b) Modify the function above so that there is an optional argument called start that allows
the list to start at a value other than 2. The function should return the first n primes that
are greater than or equal to start . The default value of start should be 2.
"""

def primes(n=10,start = 2):
    flag = True
    l = []
    while flag:
        x = 0
        for i in range(start,10000):
            for j in range(2,i-1):
                if i%j == 0:
                    break
            else:
                l.append(i)
                x += 1
            if x == n :
                flag = False
                break
    return l

num = int(input())
st = int(input())
print(primes(num,st))