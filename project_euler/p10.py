# Summation of Primes
import projecteuler as pe

sum = 5
current_number = 3
while current_number < 2000000:
    current_number = current_number + 2
    factor_list = pe.find_factors(current_number)
    if len(factor_list) == 2:
        sum = sum + current_number
print(sum)
