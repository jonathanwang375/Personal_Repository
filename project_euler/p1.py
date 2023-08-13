# Multiples of 3 or 5
limit = 1000
sum = 0
for index in range(limit):
    if (index % 3 == 0) or (index % 5 == 0):
        sum = sum + index
print(sum)
