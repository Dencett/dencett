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

def is_lucky_number(number):
    str_number = str(number)
    part = math.floor(len(str_number) / 2)
    number_part1 = sum(map(int, str_number[:part]))
    number_part2 = sum(map(int, str_number[:- part - 1:-1]))
    return number_part1 == number_part2


def is_palindromic_number(number):
    str_number = str(number)
    reverse_number = (str_number[::-1])
    return str_number == reverse_number


def is_square_number(number):
    root = number ** 0.5
    return root == int(root)


def prime_numbers_generator_filtered(n, filter_func):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            if filter_func(number):
                yield number


# for number in prime_numbers_generator_filtered(1000, is_lucky_number):
#     print(number)
#
# for number in prime_numbers_generator_filtered(1000, is_palindromic_number):
#     print(number)
#
# for number in prime_numbers_generator_filtered(1000, is_square_number):
#     print(number)


numbers_generator_filtered = list(filter(is_lucky_number, prime_numbers_generator(1000)))
for number in numbers_generator_filtered:
    print(number)

numbers_generator_filtered = list(filter(is_palindromic_number, prime_numbers_generator(1000)))
for number in numbers_generator_filtered:
    print(number)

numbers_generator_filtered = list(filter(is_square_number, prime_numbers_generator(1000)))
for number in numbers_generator_filtered:
    print(number)

# зачет!
