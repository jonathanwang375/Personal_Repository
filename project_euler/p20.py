# Factorial Digit Sum
import projecteuler as pe

number = 100
sum = 0
number = str(pe.factorial(number))
for index in range(len(number)):
    sum = sum + int(number[index])
print(sum)
