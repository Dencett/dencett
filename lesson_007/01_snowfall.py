# -*- coding: utf-8 -*-

from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, x, y, length, x_coordinate, y_coordinate):
        self.x = x
        self.y = y
        self.length = length
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def clear_previous_picture(self):
        color = sd.background_color
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=color)

    def move(self):
        self.x -= self.x_coordinate
        self.y -= self.y_coordinate

    def draw(self):
        color = sd.COLOR_WHITE
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=color)

    def can_fall(self):
        return self.y > 0


# flake = Snowflake(randint(80, 550), randint(600, 700), randint(20, 60), randint(-5, 5), randint(20, 30))
#
#
# while True:
#     sd.start_drawing()
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.finish_drawing()
#     sd.sleep(0.05)
#     if sd.user_want_exit():
#         break

# зачёт первой части


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

N = 20


def get_flakes(quantity):
    snow_list = []
    for _ in range(quantity):
        snow_list.append(Snowflake(randint(80, 550), randint(600, 700), randint(20, 60), randint(-5, 5),
                                   randint(20, 30)))
    return snow_list


flakes = get_flakes(N)
print(flakes)


def get_fallen_flakes():
    quantity = 0
    for flake in reversed(flakes):
        if not flake.can_fall():
            flakes.remove(flake)
            quantity += 1
            return quantity


def append_flakes(quantity):
    for _ in range(quantity):
        flakes.append(Snowflake(randint(80, 550), randint(600, 700), randint(20, 60), randint(-5, 5),
        randint(20, 30)))


while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        append_flakes(fallen_flakes)
    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break

sd.pause()
