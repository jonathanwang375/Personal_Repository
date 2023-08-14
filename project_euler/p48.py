# Self Powers

print("Starting Problem 48")
sum = 0
for a in range(1, 1001):
    sum = sum + a**a
test = str(sum)
print(test[-10:])