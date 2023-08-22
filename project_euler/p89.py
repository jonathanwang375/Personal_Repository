#Roman Numerals

characters_saved = 0
filename = "p089_roman.txt"
roman_list = []
with open(filename, "r") as file:
    roman_list = file.readlines()
for index in range(len(roman_list)):
    test_word = roman_list[index]
    final_word = ""
    for letter_index in range(len(final_word)):
        changed = False
        if (len(final_word) - letter_index) >= 5:
            test_substring = final_word[index:(index + 5)]
            if test_substring == "CCCCC":
                final_word = final_word + "D"
                changed = True
            elif test_substring == "XXXXX":
                final_word = final_word + "L"
                changed = True
            elif test_substring == "IIIII":
                final_word = final_word + "V"
                changed = True
        if (len(final_word) - letter_index) >=4:
            test_substring = final_word[index:(index + 4)]
            if test_substring == "CCCC":
                final_word = final_word + "CD"
                changed = True
            elif test_substring == "XXXX":
                final_word = final_word + "XL"
                changed = True
            elif test_substring == "IIII":
                final_word = final_word + "IV"
                changed = True
        if (len(final_word) - letter_index) >= 3:
            test_substring = final_word[index:(index + 3)]
            if test_substring == "DCD":
                final_word = final_word + "CM"
                changed = True
            elif test_substring == "LXL":
                final_word = final_word + "LXL"
                changed = True
            elif test_substring == "VIV":
                final_word = final_word + "IX"
                changed = True


print(characters_saved)