import projecteuler as pe
import math

print("Problem 21")
amicable_list = []
for a in range(1, 10000):
    temp1 = a
    fact_list_1 = pe.find_factors(temp1)
    tempsum1 = 0
    for b in range(0, len(fact_list_1)):
        tempsum1 = tempsum1 + fact_list_1[b]
    temp2 = tempsum1
    fact_list_2 = pe.find_factors(temp2)
    tempsum2 = 0
    for c in range(0, len(fact_list_2)):
        tempsum2 = tempsum2 + fact_list_2[c]
    if tempsum2 == temp1 and temp1 != temp2:
        amicable_list.append(temp1)
        amicable_list.append(temp2)
finalsum = 0
for d in range(0, len(amicable_list)):
    finalsum = finalsum + amicable_list[d]
print(finalsum)
