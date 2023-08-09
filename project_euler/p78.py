import projecteuler as pe
import sort
import math
from fractions import Fraction

print("Problem 71")
list = []
n = 12000
for a in range(1, n):
    for b in range((a + 1), (n + 1)):
        test = pe.gcd(b, a)
        if test == 1:
            list.append(a / b)
sort.merge_sort(list, 0, len(list) - 1)
tempindex = list.index(3 / 7)
print(list[tempindex - 1])

print("Problem 72")
print(len(list))

print("Problem 73")
tempindex1 = list.index(1 / 2)
tempindex2 = list.index(1 / 3)
num = tempindex1 - tempindex2 - 1
print(num)
