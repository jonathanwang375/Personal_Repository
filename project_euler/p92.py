print("Problem 92")
num = 1
count = 0
while num < 10000000:
    temp = num
    while temp != 89 and temp != 1:
        tempsum = 0
        temp2 = str(temp)
        for a in range(len(temp2)):
            tempsum = tempsum + int(temp2[a])
        temp = tempsum
    if temp == 89:
        count = count + 1
    num = num + 1
print(count)
