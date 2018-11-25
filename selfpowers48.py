def self_powers():
    s = 0
    for i in range(1, 1000):
        s = s + i**i
    return s
print(self_powers())


