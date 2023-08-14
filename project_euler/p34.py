# Digit Factorials
import projecteuler as pe

sum = 0
for number in range(3, 1000000):
    number_string = str(number)
    sum_test = 0
    for index in range(0, len(number_string)):
        sum_test = sum_test + pe.factorial(int(number_string[index]))
    if sum_test == number:
        sum = sum + number
print(sum)
