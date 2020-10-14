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


def draw_triangle(point, length, angle_incline):
    current_point = point
    angle0 = angle_incline
    for angle_change in range(0, 360, 120):
        angle = angle0 + angle_change
        v1 = sd.get_vector(start_point=current_point, angle=angle, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


def draw_quadrangle(point, length, angle_incline):
    current_point = point
    angle0 = angle_incline
    for angle_change in range(0, 360, 90):
        angle = angle0 + angle_change
        v1 = sd.get_vector(start_point=current_point, angle=angle, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


def draw_pentagon(point, length, angle_incline):
    current_point = point
    angle0 = angle_incline
    for angle_change in range(0, 360, 72):
        angle = angle0 + angle_change
        v1 = sd.get_vector(start_point=current_point, angle=angle, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


def draw_hexagon(point, length, angle_incline):
    current_point = point
    angle0 = angle_incline
    for angle_change in range(0, 360, 60):
        angle = angle0 + angle_change
        v1 = sd.get_vector(start_point=current_point, angle=angle, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


print('''Возможные цвета:
        0 : red
        1 : orange
        2 : yellow
        3 : green
        4 : cyan
        5 : blue
        6 : purple''')

list_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN,
               sd.COLOR_BLUE, sd.COLOR_PURPLE]

while True:
    user_input = input('Введите желаемый цвет: ')
    if user_input.isdigit():
        index = int(user_input)
        if index in range(len(list_colors)):
            color = list_colors[index]
            break
        else:
            print('Номер некорректен!')
    else:
        print('Ввод некорректен!')

point = sd.get_point(100, 100)
first_angle = 0
draw_triangle(point=point, length=150, angle_incline=first_angle)

point = sd.get_point(400, 100)
first_angle = 0
draw_quadrangle(point=point, length=120, angle_incline=first_angle)

point = sd.get_point(120, 400)
first_angle = 0
draw_pentagon(point=point, length=100, angle_incline=first_angle)

point = sd.get_point(420, 400)
first_angle = 0
draw_hexagon(point=point, length=90, angle_incline=first_angle)

sd.pause()

# зачёт! 🚀
