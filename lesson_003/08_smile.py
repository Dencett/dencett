# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smiley(x, y, color):
    radius = 50
    simple_draw.circle(center_position=simple_draw.get_point(x, y), radius=radius, color=color, width=1)
    radius -= 40
    simple_draw.circle(center_position=simple_draw.get_point(x - 25, y + 20), radius=radius,
                       color=simple_draw.COLOR_DARK_PURPLE, width=3)
    simple_draw.circle(center_position=simple_draw.get_point(x + 25, y + 20), radius=radius,
                       color=simple_draw.COLOR_DARK_PURPLE, width=3)
    simple_draw.line(start_point=simple_draw.get_point(x - 20, y - 15), end_point=simple_draw.get_point(x - 10, y - 25),
                     color=color, width=3)
    simple_draw.line(start_point=simple_draw.get_point(x - 10, y - 25), end_point=simple_draw.get_point(x + 10, y - 25),
                     color=color, width=3)
    simple_draw.line(start_point=simple_draw.get_point(x + 10, y - 25), end_point=simple_draw.get_point(x + 20, y - 15),
                     color=color, width=3)


for _ in range(10):
    color = simple_draw.COLOR_YELLOW
    x = simple_draw.random_number(0, 550)
    y = simple_draw.random_number(0, 550)
    smiley(x=x, y=y, color=color)

simple_draw.pause()

# зачёт! 🚀
