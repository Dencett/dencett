# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smiley(point, color):
    radius = 50
    simple_draw.circle(center_position=point[0], radius=radius, color=color, width=1)
    radius -= 40
    simple_draw.circle(center_position=point[1], radius=radius, color=simple_draw.COLOR_DARK_PURPLE, width=3)
    simple_draw.circle(center_position=point[2], radius=radius, color=simple_draw.COLOR_DARK_PURPLE, width=3)
    simple_draw.line(start_point=point[3], end_point=point[4], color=color, width=3)
    simple_draw.line(start_point=point[4], end_point=point[5], color=color, width=3)
    simple_draw.line(start_point=point[5], end_point=point[6], color=color, width=3)


for _ in range(10):
    color = simple_draw.COLOR_YELLOW
    x = simple_draw.random_number(0, 550)
    y = simple_draw.random_number(0, 550)
    point = [simple_draw.get_point(x, y), simple_draw.get_point(x - 25, y + 20),
             simple_draw.get_point(x + 25, y + 20), simple_draw.get_point(x - 20, y - 15),
             simple_draw.get_point(x - 10, y - 25), simple_draw.get_point(x + 10, y - 25),
             simple_draw.get_point(x + 20, y - 15)]
    smiley(point=point, color=color)

simple_draw.pause()
