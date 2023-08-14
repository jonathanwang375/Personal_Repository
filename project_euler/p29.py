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

