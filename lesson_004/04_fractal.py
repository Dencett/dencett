# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_branches(start_point, angle, length):
    if length >= 10:
        if length >= 100:
            width = 10
            color = COLOR_BROWN
        elif 70 < length < 100:
            width = 7
            color = COLOR_BROWN
        elif 30 < length <= 70:
            width = 5
            color = COLOR_BROWN
        elif length <= 30:
            width = 3
            color = sd.COLOR_DARK_GREEN
        else:
            return
    else:
        return
    delta = 30
    coefficient = .75
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v1.draw(color=color)
    next_point = v1.end_point
    next_angle = angle + delta
    next_length = length * coefficient
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    next_angle = angle - delta
    next_length = length * coefficient
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)


COLOR_BROWN = (131, 9, 0)
root_point = sd.get_point(300, 30)

draw_branches(start_point=root_point, angle=90, length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


def draw_branches(start_point, angle, length):
    if length >= 10:
        if length >= 100:
            width = 10
            color = COLOR_BROWN
        elif 70 < length < 100:
            width = 7
            color = COLOR_BROWN
        elif 30 < length <= 70:
            width = 5
            color = COLOR_BROWN
        elif length <= 30:
            width = 3
            color = sd.COLOR_DARK_GREEN
        else:
            return
    else:
        return
    delta = 30
    coefficient = .75
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v1.draw(color=color)
    next_point = v1.end_point
    next_angle = angle + delta + delta * sd.random_number(-40, 40) / 100
    next_length = length * (coefficient + coefficient * sd.random_number(-20, 20) / 100)
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    next_angle = angle - delta + delta * sd.random_number(-40, 40) / 100
    next_length = length * (coefficient + coefficient * sd.random_number(-20, 20) / 100)
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)


root_point = sd.get_point(300, 30)

draw_branches(start_point=root_point, angle=90, length=100)

sd.pause()
