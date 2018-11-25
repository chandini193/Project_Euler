#function returns the sum of multiples of 3 or 5 below n
def multiples_sum_of_3_or_5(n):
    s = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            s = s + i
    return s
n = int(input("Enter num:"))
print(multiples_sum_of_3_or_5(n))
