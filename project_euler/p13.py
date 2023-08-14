# Large Sum
import projecteuler as pe

file_name = "p013_numbers.txt"
numbers_list = []
with open(file_name, "r") as file:
    numbers_list = file.readlines()
for index in range(len(numbers_list)):
    numbers_list[index] = int(numbers_list[index])
sum = 0
for index in range(len(numbers_list)):
    sum = sum + numbers_list[index]
sum = str(sum)
print(str(sum[:10]))
