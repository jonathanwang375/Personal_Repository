# Largest Prime Factor
import projecteuler as pe

number = 600851475143
factors_list = pe.find_factors(number)
prime_list = []
for b in range(len(factors_list)):
    fact_list = pe.find_factors(factors_list[b])
    if len(fact_list) == 2:
        prime_list.append(factors_list[b])
print(prime_list[-1])
