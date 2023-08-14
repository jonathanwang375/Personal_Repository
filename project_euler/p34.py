# Digit Factorials

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
