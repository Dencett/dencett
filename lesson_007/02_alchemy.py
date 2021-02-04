# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        self.element = 'Вода'

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Mud()
        if isinstance(other, Water):
            return Lake()


class Air:

    def __init__(self):
        self.element = 'Воздух'

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Air):
            return Wind()


class Fire:

    def __init__(self):
        self.element = 'Огонь'

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Earth):
            return Lava()


class Earth:

    def __init__(self):
        self.element = 'Земля'

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Earth):
            return Pressure()


class Storm:

    def __init__(self):
        self.element = 'Шторм'

    def __str__(self):
        return self.element


class Steam:

    def __init__(self):
        self.element = 'Пар'

    def __str__(self):
        return self.element


class Mud:

    def __init__(self):
        self.element = 'Грязь'

    def __str__(self):
        return self.element


class Lightning:

    def __init__(self):
        self.element = 'Молния'

    def __str__(self):
        return self.element


class Dust:

    def __init__(self):
        self.element = 'Пыль'

    def __str__(self):
        return self.element


class Lava:

    def __init__(self):
        self.element = 'Лава'

    def __str__(self):
        return self.element


class Wind:

    def __init__(self):
        self.element = 'Ветер'

    def __str__(self):
        return self.element


class Pressure:

    def __init__(self):
        self.element = 'Давление'

    def __str__(self):
        return self.element


class Lake:

    def __init__(self):
        self.element = 'Озеро'

    def __str__(self):
        return self.element


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Water(), '+', Water(), '=', Water() + Water())
print(Air(), '+', Air(), '=', Air() + Air())
print(Earth(), '+', Earth(), '=', Earth() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
