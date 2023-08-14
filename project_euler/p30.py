# Digit Fifth Powers

list = []
for number in range(2, 10000000):
    number_string = str(number)
    sum = 0
    for index in range(len(number_string)):
        sum = sum + (int(number_string[index]) ** 5)
    if sum == number:
        list.append(number)
sum_final = 0
for index in range(len(list)):
    sum_final = sum_final + list[index]
print(sum_final)