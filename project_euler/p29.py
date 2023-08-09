# Problem 29
print("Starting Problem 29")
list = []
for a in range(2, 101):
    for b in range(2, 101):
        test = a**b
        if test not in list:
            list.append(test)
print("Problem 29")
print(len(list))
print("Starting Problem 48")
sum = 0
for a in range(1, 1001):
    sum = sum + a**a
test = str(sum)
print(test[-10:])
