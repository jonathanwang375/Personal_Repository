#Roman Numerals
import projecteuler as pe

roman_numeral_list = []
roman_numeral_value_list = []
characters_saved = 0
filename = "p089_roman.txt"
roman_list = []
with open(filename, "r") as file:
    roman_list = file.readlines()
for index in range(len(roman_list)):
    roman_list[index] = roman_list[index].strip()
for index in range(len(roman_list)):
    test_word = roman_list[index]
    number_convert = pe.convert_roman_to_number(test_word)
    string_convert = pe.convert_number_to_roman(number_convert)
    characters_saved = characters_saved + len(test_word) - len(string_convert)
print(characters_saved)