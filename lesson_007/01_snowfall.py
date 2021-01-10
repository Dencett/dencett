# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

N = 20

snow_list = []
for _ in range(N):
    snow_list.append([randint(80, 800), randint(500, 700), randint(20, 60)])
# TODO в рамках этого задания код на строках 13-15 не нужен (он реализовывается в рамках get_snowflakes(amount))


class Snowflake:
    # TODO нужен метод __init__ для инициализации исходных параметров одной снежинки (координаты и длина лучиков)
    def clear_previous_picture(self, coordinate):
        sd.start_drawing()
        self.color = sd.background_color
        self.length = coordinate[2]
        self.point = sd.get_point(coordinate[0], coordinate[1])
        sd.snowflake(center=self.point, length=self.length, color=self.color)
        sd.finish_drawing()

    def move(self, coordinate):
        coordinate[1] -= 2
        # TODO вторую координату тоже желательно менять

    def draw(self, coordinate):
        sd.start_drawing()  # TODO эти методы должны вызываться в основном цикле работы снегопада
        self.color = sd.COLOR_WHITE
        self.length = coordinate[2]
        self.point = sd.get_point(coordinate[0], coordinate[1])
        sd.snowflake(center=self.point, length=self.length, color=self.color)
        sd.finish_drawing()  # TODO в паре с этим методом

    def can_fall(self, coordinate):
        return coordinate[1] > 0  # так тоже можно
    # TODO координата -60 - слишком "низкая" для признания снежинки приземлившейся



flake = Snowflake()


# coordinate = ([randint(80, 800), randint(500, 700), randint(20, 60)])
#
# while True:
#     flake.clear_previous_picture(coordinate)
#     flake.move(coordinate)
#     flake.draw(coordinate)
#     if not flake.can_fall(coordinate):
#         break
#     sd.sleep(0.01)
#     if sd.user_want_exit():
#         break

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
snow_list = []
for _ in range(N):
    snow_list.append([randint(80, 800), randint(500, 700), randint(20, 60)])


def get_fallen_flakes():
    for coordinate in snow_list:
        if coordinate[1] == -60:  # TODO здесь нужно использовать метод can_fall
            snow_list.append([randint(80, 800), randint(500, 700), randint(20, 60)])


while True:
    for coordinate in snow_list:
        flake.clear_previous_picture(coordinate)
        flake.move(coordinate)
        flake.draw(coordinate)
    get_fallen_flakes()
    # fallen_flakes = get_fallen_flakes()
    # if fallen_flakes:
    #     append_flakes(count=fallen_flakes)
    sd.sleep(0.01)
    if sd.user_want_exit():
        break

sd.pause()