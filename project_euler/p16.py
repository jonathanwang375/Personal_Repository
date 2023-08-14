# Power Digit Sum

number = str(2**1000)
sum = 0
for index in range(len(number)):
    sum = sum + int(number[index])
print(sum)
