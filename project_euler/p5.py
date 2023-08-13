# Smallest Multiple

sum_squares = 0
sqaure_sum = 0
sum_natural_num = 0

for index in range(1, 101):
    sum_natural_num = sum_natural_num + index
    sum_squares = sum_squares + (index**2)
square_sum = sum_natural_num**2
print(square_sum - sum_squares)
