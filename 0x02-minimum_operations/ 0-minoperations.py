#!/usr/bin/python3
"""
a method calculates the fewest number of operations
needed to result in exactly n H character in the file
"""


def isPrime(number):
    """
    the function checks is a number is a prime
    """
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def minOperations(n):
    """
    the method calculating the fewest number of operations needed
    """
    prime_factors = []
    div = 2

    if not str(n).isdigit():
        return 0

    if n == 1:
        return 1
    elif (n < 1):
        return 0

    while True:
        if n % div == 0:
            prime_factors.append(div)
            n = int(n/div)
        else:
            while True:
                div += 1
                if (isPrime(div)):
                    break

        if n == 1:
            break

    minOps = sum([prime for prime in prime_factors])
    return(minOps)
