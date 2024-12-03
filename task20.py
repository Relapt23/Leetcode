# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(n):
    sub = 1
    sum = 0
    while n > 0:
        sum += n % 10
        sub *= n % 10
        n //= 10
    return sub - sum

print(subtractProductAndSum(234))