import math
#returns the value of largest prime factor of a number
def largest_prime_factor(n):
    i = 2
    ps = 0
    pb = 0
    j = math.sqrt(n)
    while i <= j:
        if n % i == 0:
            if isPrime(i):
                ps = i
                if pb < ps:
                    pb = ps     
        i = i + 1
    return pb
#checks whether the given number is prime or not
def isPrime(n):
    limit = int(math.sqrt(n) + 1)
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True
print(largest_prime_factor( 600851475143))

