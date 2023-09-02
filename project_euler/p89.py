#Roman Numerals
import projecteuler as pe

print("Program is starting")
roman_numeral_list = []
roman_numeral_value_list = []
characters_saved = 0
filename = "p089_roman.txt"
roman_list = []
with open(filename, "r") as file:
    roman_list = file.readlines()
print("This program is running")
for index in range(len(roman_list)):
    print(index)
    test_roman_numeral = roman_list[index]
    number_convert = pe.convert_roman_to_number(test_roman_numeral)
    string_convert = pe.convert_number_to_roman(number_convert)
    characters_saved = characters_saved + (len(test_roman_numeral) - len(string_convert))
print(characters_saved)