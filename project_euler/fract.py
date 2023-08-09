import projecteuler as pe
import sort as sort
import math

diff = 10000000000
print("Problem 44")
for a in range(1, 10000):
    for b in range((a + 1), 10001):
        check1 = int(pe.pentagonal_number(a))
        check2 = int(pe.pentagonal_number(b))
        sumtest = check1 + check2
        difftest = abs(check1 - check2)
        checksum = pe.check_pentagonal_number(sumtest)
        checkdiff = pe.check_pentagonal_number(difftest)
        if checksum and checkdiff:
            if diff > difftest:
                diff = difftest
print("The answer is:")
print(diff)
