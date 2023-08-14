import math


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
    result = quadratic_solver(1, 1, 2 * num)
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
    result = quadratic_solver(2, -1, num)
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
