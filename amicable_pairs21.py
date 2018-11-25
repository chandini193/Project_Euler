def is_Amicable(n):
    s = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            s += i
    return s
l = []
s = 0
for i in range(1, 10000):
    p = is_Amicable(i)
    if p > i and is_Amicable(p) == i:
        l.append(i)
        s = s + i + p
print(l)
print(s)
