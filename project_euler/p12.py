# Highly Divisible Triagular Number
import projecteuler as pe

index = 1
found = False
while not found:
    test_number = pe.triangular_number(index)
    factor_list = pe.find_factors(test_number)
    if len(factor_list) >= 500:
        found = True
    else:
        index = index + 1
print(pe.triangular_number(index))