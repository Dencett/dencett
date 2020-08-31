# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smiley(point, color):
    radius = 50
    for _ in range(1):
        simple_draw.circle(center_position=point, radius=radius, color=color, width=0)
    radius -= 42
    for _ in range(1):
        simple_draw.circle(center_position=point1, radius=radius, color=simple_draw.COLOR_DARK_PURPLE, width=3)
    for _ in range(1):
        simple_draw.circle(center_position=point2, radius=radius, color=simple_draw.COLOR_DARK_PURPLE, width=3)


for _ in range(10):
    color = simple_draw.COLOR_YELLOW
    x = simple_draw.random_number(0, 600)
    y = simple_draw.random_number(0, 600)
    point = simple_draw.get_point(x, y)
    point1 = simple_draw.get_point(x - 25, y + 25)
    point2 = simple_draw.get_point(x + 25, y + 25)
    # TODO строки 28 и 29 перенесите на 14 и 15 внутрь функции
    smiley(point=point, color=color)

simple_draw.pause()

# TODO строки до конца файла нужно удалить:
# def smiley(coordinate_x, coordinate_y, color):
#     for _ in range(1):
#         simple_draw.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=2)
#         radius = 10
#         for _ in range(1):
#             simple_draw.circle(center_position=point1, radius=radius, color=color, width=2)
#             for _ in range(1):
#                 simple_draw.circle(center_position=point2, radius=radius, color=color, width=2)
#
#
#
# for _ in range(10):
#     color = simple_draw.COLOR_YELLOW
#     x = simple_draw.random_number(0, 500)
#     y = simple_draw.random_number(0, 500)
#     left_bottom = simple_draw.get_point(x, y)
#     right_top = simple_draw.get_point(x + 150, y + 130)
#     point1 = simple_draw.get_point(x + 50, y + 100)
#     point2 = simple_draw.get_point(x + 100, y + 100)
#     smiley(coordinate_x=x, coordinate_y=y, color=color)


# Подскажите, пожалуйста, как сделать смайлик именно через параметры кордината X, координата Y,
# а то не получается через эти параметры?


# TODO здесь ваш код


