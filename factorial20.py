#returns factorial of a number
def factorial(a, n):
    if n == 1 or n == 0:
        return a
    return factorial(n * a, n -1)
#returns the sum of digits of a number
def sum_of_digits(n):
    s = 0
    while(n > 0):
        s = s + n % 10
        n = n // 10
    return s
n = factorial(1, 100)
print(sum_of_digits(n))
    
