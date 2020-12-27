# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

snow_list = []
for _ in range(20):
    snow_list.append([randint(80, 800), randint(500, 700), randint(20, 60)])


class Snowflake:
    def clear_previous_picture(self):
        sd.start_drawing()
        self.color = sd.background_color
        for coordinate in snow_list:
            self.length = coordinate[2]
            self.point = sd.get_point(coordinate[0], coordinate[1])
            sd.snowflake(center=self.point, length=self.length, color=self.color)
        sd.finish_drawing()

    def move(self):
        for self.coordinate in snow_list:
            self.coordinate[1] -= 2

    def draw(self):
        sd.start_drawing()
        self.color = sd.COLOR_WHITE
        for coordinate in snow_list:
            self.length = coordinate[2]
            self.point = sd.get_point(coordinate[0], coordinate[1])
            sd.snowflake(center=self.point, length=self.length, color=self.color)
        sd.finish_drawing()

    def can_fall(self):
        for self.coordinate in snow_list:
            if self.coordinate[1] > 10:
                return True
            else:
                return False

    # TODO здесь ваш код


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.01)
    if sd.user_want_exit():
        break

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

sd.pause()
