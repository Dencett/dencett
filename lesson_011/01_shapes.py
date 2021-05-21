# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def polygon(point, start_angle, length):
        for angle_change in range(0, 360, 360//n):
            angle = start_angle + angle_change
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
            v1.draw(color=sd.COLOR_GREEN)
            point = v1.end_point
    return polygon


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(100, 100), start_angle=13, length=150)

draw_quadrangle = get_polygon(n=4)
draw_quadrangle(point=sd.get_point(400, 100), start_angle=13, length=120)

draw_pentagon = get_polygon(n=5)
draw_pentagon(point=sd.get_point(100, 400), start_angle=13, length=100)

draw_hexagon = get_polygon(n=6)
draw_hexagon(point=sd.get_point(400, 400), start_angle=13, length=90)


sd.pause()
