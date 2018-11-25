def powers():
    l = {0}
    for i in range(2, 101):
        for j in range(2, 101):
            l.add(int(i**j))
    return len(l)
print(powers())

