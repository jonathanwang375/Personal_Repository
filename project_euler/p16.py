# Power Digit Sum

temp = str(2**1000)
sum = 0
for a in range(len(temp)):
    sum = sum + int(temp[a])
print(sum)
