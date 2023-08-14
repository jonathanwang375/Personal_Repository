# Combinatoric Selections
import projecteuler as pe

count = 0
max_limit = 100
for number_n in range(1, (max_limit + 1)):
    for number_r in range(1, (number_n + 1)):
        result_check = pe.combination(number_n, number_r)
        if result_check > 1000000:
            count = count + 1
print(count)
