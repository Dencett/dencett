# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

print('''Возможные фигуры:
        1 : треугольник
        2 : квадрат
        3 : пятиугольник
        4 : шестиугольник''')

list_figure = {1: {'point': sd.get_point(220, 250), 'length': 150, 'angle_rejection': 120},
               2: {'point': sd.get_point(220, 240), 'length': 120, 'angle_rejection': 90},
               3: {'point': sd.get_point(240, 240), 'length': 100, 'angle_rejection': 72},
               4: {'point': sd.get_point(240, 240), 'length': 90, 'angle_rejection': 60}
               }

while True:
    user_input = input('Введите желаемую фигуру: ')
    if user_input.isdigit():
        number = int(user_input)
        if number in list_figure:
            point = list_figure[number]['point']
            length = list_figure[number]['length']
            angle_rejection = list_figure[number]['angle_rejection']
            break
        else:
            print('''Номер некорректен!''')
    else:
        print('''Ввод некорректен!''')

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
# TODO словарь с целыми числами по порядку в качестве ключей это же список!
# TODO поэтому нужно отредактировать эту структуру данных и подобрать для неё более оправданный тип коллекции

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


def figure(point, length):
    current_point = point
    for angle_incline in range(0, 360, angle_rejection):
        v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point

# TODO все замечания по функции отрисовки фигуры см. в 01_shapes.py


figure(point=point, length=length)


# def triangle(point, length):
#     current_point = point
#     for angle_incline in range(0, 360, 120):
#         v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
#         v1.draw(color=color)
#         current_point = v1.end_point
#
#
# point = sd.get_point(100, 100)
# triangle(point=point, length=150)
#
#
# def quadrangle(point, length):
#     current_point = point
#     for angle_incline in range(0, 360, 90):
#         v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
#         v1.draw(color=color)
#         current_point = v1.end_point
#
#
# point = sd.get_point(400, 100)
# quadrangle(point=point, length=120)
#
#
# def pentagon(point, length):
#     current_point = point
#     for angle_incline in range(0, 360, 72):
#         v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
#         v1.draw(color=color)
#         current_point = v1.end_point
#
#
# point = sd.get_point(120, 400)
# pentagon(point=point, length=100)
#
#
# def hexagon(point, length):
#     current_point = point
#     for angle_incline in range(0, 360, 60):
#         v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
#         v1.draw(color=color)
#         current_point = v1.end_point
#
#
# point = sd.get_point(420, 400)
# hexagon(point=point, length=90)

sd.pause()
