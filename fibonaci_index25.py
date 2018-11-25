#returns the index of 1000 digits fibonacci number
def fibonacci():
    f = s =1	
    t = f + s
    c = 3
    while(num_of_digits(t) != 1000):
        f = s
        s = t
        t = f + s
        c = c + 1
    return c
#returns the number of digits in a numberS
def num_of_digits(n):
    c = 0
    while(n > 0):
        c = c + 1
        n = n // 10
    return c
print(fibonacci())
