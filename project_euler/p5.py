# Smallest Multiple

found = False
number = 20
while not found:
    divisible = True
    for index in range(1, 21):
        if number % index != 0:
            divisible = False
    if divisible:
        found = True
    else:
        number = number + 1
print(number)
