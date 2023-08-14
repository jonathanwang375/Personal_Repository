# Longest Collatz Sequence

index_max_length = 0
max_length = 0
for index in range(2, 1000000):
    test_number = index
    current_length = 1
    while test_number != 1:
        if test_number % 2 == 0:
            test_number = int(test_number / 2)
        else:
            test_number = 3 * test_number + 1
        current_length = current_length + 1
    if current_length > max_length:
        max_length = current_length
        index_max_length = index
print(index_max_length)
