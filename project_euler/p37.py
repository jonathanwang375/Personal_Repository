# Truncatable Primes
import projecteuler as pe

limit = 1000000
sum = 0
for number in range(9, limit, 2):
    number_string = str(number)
    prime = True
    for index in range(1, len(number_string) + 1):
        test_number = int(number_string[:index])
        factor_list = pe.find_factors(number)
        if len(factor_list) != 2:
            prime = False
    for index in range(1, len(number_string) + 1):
        test_number = int(number_string[(-1 * index) :])
        factor_list = pe.find_factors(test_number)
        if len(factor_list) != 2:
            prime = False
    if prime:
        sum = sum + number
print(sum)
