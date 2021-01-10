# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from termcolor import cprint


class Resident:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return '{}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def relax(self):
        cprint('{} отдыхал'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            if self.house.food <= 10:
                cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
                self.house.money -= 50
                self.house.food += 50
            if self.house.cat_food <= 20:
                cprint('{} сходил в магазин за кошачьей едой'.format(self.name), color='magenta')
                self.house.money -= 50
                self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleaning(self):
        cprint('{} убрался в доме'.format(self.name), color='magenta')
        self.house.mud -= 100
        if self.house.mud < 0:
            self.house.mud = 0
        self.fullness -= 20

    def resident_house(self, house):
        self.house = house

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness <= 30:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food < 30:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.cleaning()
        else:
            self.relax()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return '{}, сытость {}'.format(
            self.name, self.fullness,
        )

    def sleep(self):
        cprint('{} поспал.'.format(self.name), color='green')
        self.fullness -= 10

    def pick_cat(self, house):
        self.house = house
        cprint('Хозяин подобрал кота, дал имя "{}"'.format(self.name), color='cyan')

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.cat_food -= 10
        else:
            cprint('{} мяукает, нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def tear_wallpaper(self):
        cprint('{} дерет обои'.format(self.name), color='yellow')
        self.house.mud += 5
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tear_wallpaper()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 0
        self.money = 100
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьей еды {}, денег осталось {}, грязи {}'.format(
            self.food, self.cat_food, self.money, self.mud
        )


householder = Resident(name='Хозяин')
house = House()
householder.resident_house(house=house)

# pet = Cat(name='Барсик')
# pet.pick_cat(house=house)
#
# for day in range(1, 366):
#     print('================ день {} =================='.format(day))
#     householder.act()
#     pet.act()
#     print('--- в конце дня ---')
#     print(householder)
#     print(pet)
#     print(house)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

cats = [
    Cat(name='Барсик'),
    Cat(name='Мурзик'),
    Cat(name='Снежок'),
]

for cat in cats:
    cat.pick_cat(house=house)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    householder.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    print(householder)
    for cat in cats:
        print(cat)
    print(house)


# (Можно определить критическое количество котов, которое может прокормить человек...)
