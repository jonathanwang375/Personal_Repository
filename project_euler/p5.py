# Smallest Multiple
import projecteuler as pe

number = 20
prime_list = []
prime_count_list = []
for number in range(1, (number + 1)):
    if pe.is_prime(number) and number not in prime_list:
        prime_list.append(number)
print(prime_list)