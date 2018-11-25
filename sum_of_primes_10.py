import math
#returns the sum of prime numbers below limit 
def sum_of_primes(limit):
    sum = 0
    for i in range(2, limit):
        if isPrime(i):
           sum = sum + i
    return sum
#checks whether the given number is prime or not
def isPrime(n):
    limit = int(math.sqrt(n) + 1)
    for i in range(2,limit):
        if n % i == 0:
            return False
    return True
print(sum_of_primes(2000000))
