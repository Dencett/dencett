# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел

import math


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# for number in get_prime_numbers(10000):
#     print(number)

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.prime_numbers = []
        self.number_of_iterations = n
        self.iteration = 0

    def __iter__(self):
        self.iteration = 1
        return self

    def __next__(self):
        while self.iteration < self.number_of_iterations:
            self.iteration += 1
            for prime in self.prime_numbers:
                if self.iteration % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.iteration)
                return self.iteration
        else:
            raise StopIteration()


# prime_number_iterator = PrimeNumbers(n=10)
# for number in prime_number_iterator:
#     print(number)

# зачет!

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# for number in prime_numbers_generator(n=10000):
#     print(number)

# зачет!

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def lucky_numbers_generator(number):
    str_number = str(number)
    part = math.floor(len(str_number) / 2)
    number_part1 = sum(map(int, str_number[:part]))
    number_part2 = sum(map(int, str_number[:- part - 1:-1]))
    return number_part1 == number_part2


def check_palindromic_numbers(number):
    str_number = str(number)
    reverse_number = (str_number[::-1])
    return str_number == reverse_number


def check_square_numbers(number):
    root = number ** 0.5
    return root == int(root)


def get_numbers_generator(quantity):
    for number in range(1, quantity + 1):
        if lucky_numbers_generator(number) \
                and check_palindromic_numbers(number) \
                and check_square_numbers(number) is True:
            yield number


for number in get_numbers_generator(100000):
    print(number)
