import math

print("Starting Problem 30")
list = []
for a in range(0, 10000000):
    test = str(a)
    sum = 0
    for b in range(0, len(test)):
        sum = sum + math.pow(int(test[b]), 5)
    if sum == a:
        list.append(a)
finalsum = 0
for c in range(0, len(list)):
    finalsum = finalsum + list[c]
print("Problem 30")
print(list)
print(finalsum)

print("Starting Problem 34")
factlist = []
for d in range(0, 100000000):
    test = str(d)
    sumfact = 0
    for e in range(0, len(test)):
        sumfact = sumfact + math.factorial(int(test[e]))
    if sumfact == d:
        factlist.append(d)
finalsumfact = 0
for f in range(0, len(factlist)):
    finalsumfact = finalsumfact + factlist[f]
finalsumfact = finalsumfact - 2 - 1
print("Problem 34")
print(factlist)
print(finalsumfact)
