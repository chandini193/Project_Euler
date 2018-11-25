#returns the value of the number which is divisible by all the numbers below 20
def smallest_multiple():
    i = 1
    while True:
        if i % 20 == 0 and i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and i % 16 == 0 and i % 15 == 0 and i % 14 == 0 and i % 13 == 0 and i % 12 == 0 and i % 11 == 0:
            return i
        i = i + 1
print(smallest_multiple())
