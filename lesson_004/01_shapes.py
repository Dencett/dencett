# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
color = sd.COLOR_ORANGE


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


def pentagon(point, length):
    current_point = point
    for angle_incline in range(0, 360, 60):
        v1 = sd.get_vector(start_point=current_point, angle=angle_incline, length=length, width=4)
        v1.draw(color=color)
        current_point = v1.end_point


point = sd.get_point(420, 400)
pentagon(point=point, length=90)



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
