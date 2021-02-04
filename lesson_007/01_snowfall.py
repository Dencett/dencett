# -*- coding: utf-8 -*-

from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, coordinate):
        self.coordinate = coordinate

    def clear_previous_picture(self):
        sd.start_drawing()
        self.color = sd.background_color
        self.length = coordinate[2]
        self.point = sd.get_point(coordinate[0], coordinate[1])
        sd.snowflake(center=self.point, length=self.length, color=self.color)
        sd.finish_drawing()

    def move(self, change_coordinate):
        coordinate[1] -= change_coordinate

    def draw(self):
        self.color = sd.COLOR_WHITE
        self.length = coordinate[2]
        self.point = sd.get_point(coordinate[0], coordinate[1])
        sd.snowflake(center=self.point, length=self.length, color=self.color)

    def can_fall(self):
        return coordinate[1] > 0  # так тоже можно


# TODO эти параметры снежинки должны быть в конструкторе (метод __init__)
coordinate = ([randint(80, 800), randint(500, 700), randint(20, 60)])
flake = Snowflake(coordinate)  # TODO передавать их как аргумент - подход неверный
# TODO при создании массива снежинок это создаст ненужную путаницу
#  а так, если все координаты и длины для каждой снежинки - "внутри" её самой спрятаны - будет гораздо проще

while True:
    sd.start_drawing()
    flake.clear_previous_picture()
    flake.move(randint(1, 4))
    flake.draw()
    if not flake.can_fall():
        break
    sd.finish_drawing()
    sd.sleep(0.01)
    if sd.user_want_exit():
        break

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

# N = 20
#
#
# def get_flakes(coordinate):
#     snow_list = []
#     for _ in range(coordinate):
#         snow_list.append([randint(80, 800), randint(500, 700), randint(20, 60)])
#     return snow_list


# flakes = get_flakes(N)
#
#
# flake = Snowflake(snow_list)
# def get_fallen_flakes():
#     for coordinate in snow_list:
#         if not flake.can_fall():  # TODO здесь нужно использовать метод can_fall
#             snow_list.append([randint(80, 800), randint(500, 700), randint(20, 60)])
#             # flake = Snowflake(coordinate)
#
#
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     get_fallen_flakes()
#     fallen_flakes = get_fallen_flakes()
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)
#     sd.sleep(0.01)
#     if sd.user_want_exit():
#         break

sd.pause()
