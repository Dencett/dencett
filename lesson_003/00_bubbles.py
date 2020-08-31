# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(400, 200)
radius = 50
COLOR_DARK_RED = (127, 0, 0)
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, color=COLOR_DARK_RED, width=2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=3)

point = sd.get_point(400, 200)
COLOR_DARK_RED = (127, 0, 0)
color = COLOR_DARK_RED
bubble(point=point, step=10, color=color)
#
# # Нарисовать 10 пузырьков в ряд
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=3)

for x in range(100, 1100, 100):
    point = sd.get_point(x, 200)
    COLOR_DARK_RED = (127, 0, 0)
    color = COLOR_DARK_RED
    bubble(point=point, step=5, color=color)
#
# # Нарисовать три ряда по 10 пузырьков
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=3)

for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        COLOR_DARK_RED = (127, 0, 0)
        color = COLOR_DARK_RED
        bubble(point=point, step=5, color=color)
#
# # Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=3)

for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bubble(point=point, step=5, color=color)

sd.pause()
