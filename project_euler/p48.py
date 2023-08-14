# Self Powers

sum = 0
for number in range(1, 1001):
    sum = sum + number**number
sum_string = str(sum)
print(sum_string[-10:])
