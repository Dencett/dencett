# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
print('''Возможные цвета:
        1 : red
        2 : orange
        3 : yellow
        4 : green
        5 : cyan
        6 : blue
        7 : purple''')

list_colors = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE, 3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN, 5: sd.COLOR_CYAN,
               6: sd.COLOR_BLUE, 7: sd.COLOR_PURPLE}
while True:
    user_input = input('Введите желаемый цвет: ')
    if user_input.isdigit():
        color = int(user_input)
        if color in list_colors:
            color = list_colors[color]
            break
        else:
            print('''Номер некорректен!''')
    else:
        print('''Ввод некорректен!''')


def triangle(point, length):
    current_point = point
    for angle_incline in range(0, 360, 120):
        v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


point = sd.get_point(100, 100)
triangle(point=point, length=150)


def quadrangle(point, length):
    current_point = point
    for angle_incline in range(0, 360, 90):
        v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


point = sd.get_point(400, 100)
quadrangle(point=point, length=120)


def pentagon(point, length):
    current_point = point
    for angle_incline in range(0, 360, 72):
        v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


point = sd.get_point(120, 400)
pentagon(point=point, length=100)


def hexagon(point, length):
    current_point = point
    for angle_incline in range(0, 360, 60):
        v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


point = sd.get_point(420, 400)
hexagon(point=point, length=90)

sd.pause()
