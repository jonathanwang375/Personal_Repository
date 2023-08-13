# Largest Palindrome Product
import projecteuler as pe

max_palindrome_num = 0
test_num = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        test_num = a * b
        test_palindrome = pe.ispalindrome(test_num)
        if test_palindrome and test_num > max_palindrome_num:
            max_palindrome_num = test_num
print(max_palindrome_num)
