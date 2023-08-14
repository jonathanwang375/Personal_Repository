# Pentagon Numbers
import projecteuler as pe

diff = 10000000000
for number_1 in range(1, 10000):
    for number_2 in range((number_1 + 1), 10001):
        pent_num_1 = pe.pentagonal_number(number_1)
        pent_num_2 = pe.pentagonal_number(number_2)
        sum_check = pent_num_1 + pent_num_2
        diff_check = abs(pent_num_2 - pent_num_1)
        check_sum_pent = pe.check_pentagonal_number(sum_check)
        check_diff_pent = pe.check_pentagonal_number(diff_check)
        if check_sum_pent and check_diff_pent:
            if diff > diff_check:
                diff = diff_check
print(diff)
