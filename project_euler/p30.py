# Digit Fifth Powers

list = []
sum_final = 0
for number in range(2, 10000000):
    number_string = str(number)
    sum = 0
    for index in range(len(number_string)):
        sum = sum + (int(number_string[index]) ** 5)
    if sum == number:
        sum_final = sum_final + number
print(sum_final)
