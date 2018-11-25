#checks whether the given number is palindrome or not
def isPalindrome(n):
    t = n
    rev = 0
    while(t > 0):
        rev = rev * 10 + t % 10
        t = t // 10
    return n == rev
#returns largest palindrome that can be written as product of 3 digit numbers
def largest_palindrome_product():
    l = []
    for i in range(100,1000):
        for j in range(100, 1000):
            p = i * j
            if isPalindrome(p):
               l.append((p))
    return l
print(max(largest_palindrome_product()))
                   

