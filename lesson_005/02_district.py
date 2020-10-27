# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


# people = []

from district.central_street.house1 import room1
from district.central_street.house1 import room2
central_house1 = room1.folks + room2.folks
from district.central_street.house2 import room1
from district.central_street.house2 import room2
central_house2 = room1.folks + room2.folks
from district.soviet_street.house1 import room1
from district.soviet_street.house1 import room2
soviet_house1 = room1.folks + room2.folks
from district.soviet_street.house2 import room1
from district.soviet_street.house2 import room2
soviet_house2 = room1.folks + room2.folks

people = central_house1 + central_house2 + soviet_house1 + soviet_house2

print('На районе живут', ', ' .join(people))


# TODO здесь ваш код
