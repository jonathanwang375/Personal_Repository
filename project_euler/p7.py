# 10001st Prime
import projecteuler as pe

number = 3
count = 2
while count != 10001:
    number = number + 2
    factor_list = pe.find_factors(number)
    if len(factor_list) == 2:
        count = count + 1
print(number)
