import math
#checks whether the given number is prime or not
def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
#returns the value of 1001 prime number
def prime():
    i = 2
    c = 0
    while True:
        if isPrime(i):
            c = c + 1
        if c == 10001:
            return i
        i = i + 1
print(prime())
