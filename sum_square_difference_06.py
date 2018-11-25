#returns the sum square difference with in the limit
def sum_square_difference(limit):
    sum = 0
    square_sum = 0
    for i in range(1,limit+1):
        sum = sum + i
        square_sum = square_sum + i**2
    return (sum ** 2 - square_sum)
print(sum_square_difference(100))
