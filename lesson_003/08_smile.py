# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smiley(point, color):
    radius = 50
    # TODO все координаты можно сохранить в список без создания отдельных переменных
    point1 = simple_draw.get_point(x - 25, y + 20)
    point2 = simple_draw.get_point(x + 25, y + 20)
    point3 = simple_draw.get_point(x - 20, y - 15)
    point4 = simple_draw.get_point(x - 10, y - 25)
    point5 = simple_draw.get_point(x + 10, y - 25)
    point6 = simple_draw.get_point(x + 20, y - 15)
    # TODO далее в этом методе циклы не нужны. Какой смысл в них, если задавать только одну итерацию? :)
    for _ in range(1):
        simple_draw.circle(center_position=point, radius=radius, color=color, width=1)
    radius -= 40
    for _ in range(1):
        simple_draw.circle(center_position=point1, radius=radius, color=simple_draw.COLOR_DARK_PURPLE, width=3)
    for _ in range(1):
        simple_draw.circle(center_position=point2, radius=radius, color=simple_draw.COLOR_DARK_PURPLE, width=3)
    for _ in range(1):
        simple_draw.line(start_point=point3, end_point=point4, color=color, width=3)
    for _ in range(1):
        simple_draw.line(start_point=point4, end_point=point5, color=color, width=3)
    for _ in range(1):
        simple_draw.line(start_point=point5, end_point=point6, color=color, width=3)


for _ in range(10):
    color = simple_draw.COLOR_YELLOW
    x = simple_draw.random_number(0, 550)
    y = simple_draw.random_number(0, 550)
    point = simple_draw.get_point(x, y)
    smiley(point=point, color=color)

simple_draw.pause()
