import math

alphabet_list = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

def find_factors(num):
    list = []
    for a in range(1, int(math.sqrt(num)) + 1, 1):
        if num % a == 0:
            list.append(a)
            list.append(int(num / a))
    return list


def triangular_number(num):
    test = (num) * (num + 1) * (1 / 2)
    return int(test)


def pentagonal_number(num):
    test = (3 * num - 1) * (num) * (1 / 2)
    return int(test)


def hexagonal_number(num):
    test = (2 * num) * (2 * num + 1) * (1 / 2)
    return int(test)


def check_triangular_number(num):
    result = quadratic_solver(1, 1, -2 * num)
    final = False
    if len(result) == 2:
        if (result[0] > 0 and result[0] % 1 == 0) or (
            result[1] > 0 and result[1] % 1 == 0
        ):
            final = True
    return final


def check_pentagonal_number(num):
    result = quadratic_solver(3, -1, -2 * num)
    final = False
    if len(result) == 2:
        if (result[0] > 0 and result[0] % 1 == 0) or (
            result[1] > 0 and result[1] % 1 == 0
        ):
            final = True
    return final


def check_hexagonal_number(num):
    result = quadratic_solver(2, -1, -1 * num)
    final = False
    if len(result) == 2:
        if (result[0] > 0 and result[0] % 1 == 0) or (
            result[1] > 0 and result[1] % 1 == 0
        ):
            final = True
    return final


def quadratic_solver(a, b, c):
    solutions = []
    delta = pow(b, 2) - (4 * a * c)
    if delta < 0:
        return solutions
    else:
        x1 = (-1 * b) + math.sqrt(delta)
        x1 = x1 / (2 * a)
        x2 = (-1 * b) - math.sqrt(delta)
        x2 = x2 / (2 * a)
        solutions.append(x1)
        solutions.append(x2)
        return solutions


def txt_to_file(filename):
    file = open(filename, "r")
    temp = file.read()
    list = temp.split(",")
    for a in range(0, len(list)):
        list[a] = list[a].replace('"', "")
    return list


def ispalindrome(num):
    test = str(num)
    count = 0
    if len(test) % 2 == 1:
        count = len(test) // 2
    else:
        count = int(len(test) / 2)
    palin = True
    while count > 0 and palin:
        end = len(test) - count
        if test[count - 1] == test[end]:
            palin = True
        else:
            palin = False
        count = count - 1
    return palin


def gcd(a, b):
    while a > b:
        a = a - b
    return a


def fib_num(term_a: int, term_b: int):
    new_term_a = term_b
    new_term_b = term_a + term_b
    return new_term_a, new_term_b


def factorial(number: int):
    result = 1
    for index in range(2, (number + 1)):
        result = result * index
    return result


def combination(n: int, k: int):
    n_fact = factorial(n)
    k_fact = factorial(k)
    nk_fact = factorial(n - k)
    result = n_fact / (k_fact * nk_fact)
    return result


def convert_character_to_number(character: str):
    result = alphabet_list.index(character)
    return int(result + 1)

def convert_roman_to_number(roman_string: str) -> int:
    number_result = 0
    string_index = 0
    while (string_index <= (len(roman_string) - 1)):
        if roman_string[string_index] == "I":
            if ((string_index + 1) < len(roman_string)):
                if roman_string[string_index + 1] == "V":
                    number_result = number_result + 4
                    string_index = string_index + 2
                elif roman_string[string_index + 1] == "X":
                    number_result = number_result + 9
                    string_index = string_index + 2
                else:
                    number_result = number_result + 1
                    string_index = string_index + 1
            else:
                number_result = number_result + 1
                string_index = string_index + 1
        elif roman_string[string_index] == "V":
            number_result = number_result + 5
            string_index = string_index + 1
        elif roman_string[string_index] == "X":
            if ((string_index + 1) < len(roman_string)):
                if roman_string[string_index + 1] == "L":
                    number_result = number_result + 40
                    string_index = string_index + 2
                elif roman_string[string_index + 1] == "C":
                    number_result = number_result + 90
                    string_index = string_index + 2
                else:
                    number_result = number_result + 10
                    string_index = string_index + 1
            else:
                number_result = number_result + 10
                string_index = string_index + 1
        elif roman_string[string_index] == "L":
            number_result = number_result + 50
            string_index = string_index + 1
        elif roman_string[string_index] == "C":
            if ((string_index + 1) < len(roman_string)):
                if roman_string[string_index + 1] == "D":
                    number_result = number_result + 400
                    string_index = string_index + 2
                elif roman_string[string_index + 1] == "M":
                    number_result = number_result + 900
                    string_index = string_index + 2
                else:
                    number_result = number_result + 100
                    string_index = string_index + 1
            else: 
                number_result = number_result + 100
                string_index = string_index + 1
        elif roman_string[string_index] == "D":
            number_result = number_result + 500
            string_index = string_index + 1
        elif roman_string[string_index] == "M":
            number_result = number_result + 1000
            string_index = string_index + 1
    return number_result


def convert_number_to_roman(number: int) -> str:
    roman_result = ""
    while (number != 0):
        if number >= 1000:
            roman_result = roman_result + "M"
            number = number - 1000
        elif number >= 900:
            roman_result = roman_result + "CM"
            number = number - 900
        elif number >= 500:
            roman_result = roman_result + "D"
            number = number - 500
        elif number >= 400:
            roman_result = roman_result + "CD"
            number = number - 400
        elif number >= 100:
            roman_result = roman_result + "C"
            number = number - 100
        elif number >= 90:
            roman_result = roman_result + "XC"
            number = number - 90
        elif number >= 50:
            roman_result = roman_result + "L"
            number = number - 50
        elif number >= 40:
            roman_result = roman_result + "XL"
            number = number - 40
        elif number >= 10:
            roman_result = roman_result + "X"
            number = number - 10
        elif number >= 9:
            roman_result = roman_result + "IX"
            number = number - 9
        elif number >= 5:
            roman_result = roman_result + " V"
            number = number - 5
        elif number >= 4:
            roman_result = roman_result + "IV"
            number = number - 4
        elif number >= 1:
            roman_result = roman_result + "I"
            number = number - 1
    return roman_result