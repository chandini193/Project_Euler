import math
def fact_sum(n):
    t = n
    s = 0
    while t > 0:
        s = s + math.factorial(t%10)
        t //= 10
    return s == n
l = []
sum = 0
for i in range(3, 100000):
    if fact_sum(i):
        l.append(i)
        sum = sum + i
print(sum)
print(l)

        

