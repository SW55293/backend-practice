'''
Divide N by two as many times as you can do so evenly (no remainder). 
For each division, append a 2 to the list of prime factors
At this point, N must be odd. Start a loop that iterates over all odd numbers from 3 to the square root of N inclusive.
For each number i, if i can divide evenly into N, then divide N by i and append i to the list. 
Repeat this (nested loop) until i can't divide evenly into N, then move on to the next i
If N is still greater than 2 after that loop, it must still be prime, so just append it to the list.
Return the list of primes

'''
def prime_factors(n):

    prime_factors = []

    # Divide by 2 as many times as possible
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    # Check for odd factors from 3 to the square root of n
    for x in range(3, int(n**0.5) + 1, 2):
        while n % x == 0:
            prime_factors.append(x)
            n //= x

    # If n is still greater than 2, it is a prime factor
    if n > 2:
        prime_factors.append(n)

    return prime_factors  