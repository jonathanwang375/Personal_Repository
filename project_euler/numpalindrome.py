import math
import projecteuler as pe

maxpalin = 0
test = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        test = a * b
        testpalin = pe.ispalindrome(test)
        if testpalin and test > maxpalin:
            maxpalin = test
print(maxpalin)
