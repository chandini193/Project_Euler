def power_4sum(n):
    s = 0
    t = n
    while t > 0:
        s = s + ((t%10)**5)
        t //=  10
    return n == s
l = []
for i in range(1, 1000000):
    if power_4sum(i):
        l.append(i)
print(l)
s = 0
for i in l:
    s = s + i
print(s)
