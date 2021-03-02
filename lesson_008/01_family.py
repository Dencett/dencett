# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    money = 100
    food = 50
    cat_food = 30
    mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, грязи {}'.format(
            House.food, House.money, House.mud
        )

    def mud_increase(self):
        House.mud += 5
        return House.mud


class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return '{}, сытость {}, счастье {}'.format(
            self.name, self.fullness, self.happiness
        )

    def act(self):
        if House.mud >= 90:
            self.happiness -= 10
        if self.fullness <= 0:
            cprint('{} умер(ла) от голода'.format(self.name), color='red')
            return True
        if self.happiness <= 0:
            cprint('{} умер(ла) от депрессии'.format(self.name), color='red')
            return True
        else:
            return False

    def eat(self):
        dice = randint(1, 3)
        if dice == 1:
            desire_to_eat = 30
        elif dice == 2:
            desire_to_eat = 20
        else:
            desire_to_eat = 10
        if House.food >= desire_to_eat:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += desire_to_eat
            House.food -= desire_to_eat
            Outcome.food_eaten += desire_to_eat
            return House.food, Outcome.food_eaten
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def pet_the_cat(self):
        cprint('{} погладил(а) кота'.format(self.name), color='green')
        self.happiness += 5
        self.fullness -= 10


class Husband(Human):

    def act(self):
        if super().act():
            return True
        else:
            dice = randint(1, 4)
            if self.fullness <= 20:
                self.eat()
            elif House.money < 100:
                self.work()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            elif dice == 3:
                self.pet_the_cat()
            else:
                self.gaming()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.fullness -= 10
        House.money += 150
        Outcome.earned_money += 150
        return House.money, Outcome.earned_money

    def gaming(self):
        cprint('{} поиграл в World of Tanks'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20


class Wife(Human):

    def act(self):
        if super().act():
            return True
        else:
            dice = randint(1, 7)
            if self.fullness <= 20:
                self.eat()
            elif House.food <= 60:
                self.shopping()
            elif House.cat_food <= 10:
                self.shopping()
            elif House.mud >= 100:
                self.clean_house()
            elif dice == 1 and 2:
                self.eat()
            elif dice == 3 and 4:
                self.shopping()
            elif dice == 5:
                self.clean_house()
            elif dice == 6:
                self.pet_the_cat()
            else:
                self.buy_fur_coat()

    def shopping(self):
        if House.money >= 50:
            if House.food <= 60:
                House.money -= 50
                House.food += 50
                cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            if House.cat_food <= 10:
                cprint('{} купила коту еды'.format(self.name), color='magenta')
                House.money -= 50
                House.cat_food += 50
            self.fullness -= 10
            return House.money, House.food, House.cat_food
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.fullness -= 10

    def buy_fur_coat(self):
        if House.money >= 350:
            cprint('{} купила шубу'.format(self.name), color='green')
            self.fullness -= 10
            self.happiness += 60
            House.money -= 350
            Outcome.fur_coats += 1
            return House.money, Outcome.fur_coats
        else:
            cprint('{} загрустила, денег не хватило!'.format(self.name), color='red')
            self.fullness -= 10
            self.happiness -= 10

    def clean_house(self):
        cprint('{} убралась в доме'.format(self.name), color='magenta')
        House.mud -= 100
        if House.mud < 0:
            House.mud = 0
        self.fullness -= 20
        return House.money


class Outcome:
    earned_money = 0
    food_eaten = 0
    fur_coats = 0

    def __str__(self):
        return 'Итого заработано денег: {}, съедено еды: {}, куплено шуб {}'.format(
            Outcome.earned_money, Outcome.food_eaten, Outcome.fur_coats
        )


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# outcome = Outcome()
#
# for day in range(1, 366):
#     home.mud_increase()
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#
# cprint(outcome, color='yellow')

# зачёт первой части


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30

    def __str__(self):
        return '{}, сытость {}'.format(
            self.name, self.fullness
        )

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if House.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            House.cat_food -= 5
            return House.cat_food
        else:
            cprint('{} мяукает, нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def sleep(self):
        cprint('{} поспал.'.format(self.name), color='green')
        self.fullness -= 10

    def soil(self):
        cprint('{} дерет обои'.format(self.name), color='yellow')
        House.mud += 5
        self.fullness -= 10
        return House.mud


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if House.food >= 10:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += 10
            House.food -= 10
            Outcome.food_eaten += 10
            return House.food, Outcome.food_eaten
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def sleep(self):
        cprint('{} поспал.'.format(self.name), color='green')
        self.fullness -= 10


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
outcome = Outcome()

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

cprint(outcome, color='yellow')

# зачёт второй части бис
# зачёт! 🚀

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
