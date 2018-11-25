#returns the value 2 power 1000
def power():
    n = 2**1000
    return n
#returns the sum of digits of a number
def power_digit_sum(n):
    s = 0
    while(n > 0):
        s = s + n % 10
        n = n // 10
    return s
n = power()
print(n)
print(power_digit_sum(n))
