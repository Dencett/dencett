# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint, choice


ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):

    def __str__(self):
        return 'Я бог'


class DrunkError(Exception):

    def __str__(self):
        return 'Пьяный'


class CarCrashError(Exception):

    def __str__(self):
        return 'Автомобильная авария'


class GluttonyError(Exception):

    def __str__(self):
        return 'Чревоугодие'


class DepressionError(Exception):

    def __str__(self):
        return 'Депрессия'


class SuicideError(Exception):

    def __str__(self):
        return 'Самоубийство'


day = 0
total_carma = 0
list_exc = (IamGodError, DrunkError, CarCrashError,
            GluttonyError, DepressionError, SuicideError)


def one_day():
    carma = randint(1, 7)
    dice = randint(1, 13)
    if dice == 1:
        exc = choice(list_exc)
        raise exc
    return carma


while total_carma < ENLIGHTENMENT_CARMA_LEVEL:
    day += 1
    print(day)
    carma = 0
    try:
        carma += one_day()
    except list_exc as exc:
        print(f'Состояние: {exc}')
    else:
        total_carma += carma


# https://goo.gl/JnsDqu

# зачет!
