import math

print("Problem 686")
count = 0
power = 7
while count < 678910:
    temp1 = 2**power
    temp2 = str(temp1)
    if temp2[:3] == "123":
        count = count + 1
    power = power + 1
print(power)
