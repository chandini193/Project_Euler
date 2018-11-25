#returns the sum of even fibonacci numbers sum with in the limit
def even_fibonacci_sum(limit):
    f = 0
    s = 1
    sum = 0
    for i in range(limit):
        t = f + s
        if t % 2 == 0:
            sum = sum + t
        if sum >= limit:
            return sum
        f = s
        s = t
print(even_fibonacci_sum(4000000))
