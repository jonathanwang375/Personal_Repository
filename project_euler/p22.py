import projecteuler as pe
import sort
import math

print("Problem 22")
list = pe.txt_to_file("p022_names.txt")
sort.merge_sort(list, 0, len(list) - 1)
sum = 0
for a in range(0, len(list)):
    temp = list[a].lower()
    tempsum = 0
    for b in range(0, len(temp)):
        tempsum = tempsum + ord(temp[b]) - 96
    sum = sum + ((a + 1) * tempsum)
print(sum)
