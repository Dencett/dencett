# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def figure(point, length, angle_incline):
    current_point = point
    angle0 = angle_incline
    for angle_change in range(0, 360, angle_rejection):
        angle = angle0 + angle_change
        v1 = sd.get_vector(start_point=current_point, angle=angle, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


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

first_angle = 0
figure(point=point, length=length, angle_incline=first_angle)

sd.pause()

# зачёт! 🚀
