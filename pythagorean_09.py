#returns the pythagorean triplet whose sum is 1000
def pythagorean(l):
    for i in range(1,1000):
        for j in range(1,1000):
            for k in range(1,1000):
                if i*i + j*j == k*k and i + j + k == 1000 and i < j < k:
                    l.append((i,j,k))
                    if len(l) == 1:
                        return l
l =[]
print(pythagorean(l))
print(l[0][0] * l[0][1] * l[0][2])
