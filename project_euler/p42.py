# Coded Triangle Numbers
import projecteuler as pe

count = 0
word_list = pe.txt_to_file("p042_words.txt")
for word in word_list:
    sum_test = 0
    for index in range(len(word)):
        sum_test = sum_test + pe.convert_character_to_number(word[index])
    triange_test = pe.check_triangular_number(sum_test)
    if triange_test:
        count = count + 1
print(count)
