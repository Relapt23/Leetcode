# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

def smallestEvenMultiple(n):
    i = n
    while True:
        if i % n == 0 and i % 2 == 0:
            return i
        i += 1

print(smallestEvenMultiple(5))