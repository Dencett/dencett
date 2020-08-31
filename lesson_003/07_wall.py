# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


length = 100
width = 50
y = 0
y1 = width
for i in range(14):
    start_point = simple_draw.get_point(0, y)
    end_point = simple_draw.get_point(600, y)
    simple_draw.line(start_point=start_point, end_point=end_point, color=simple_draw.COLOR_CYAN, width=1)
    if i % 2 == 1:
        x1 = 0
        x2 = length
        for _ in range(7):
            left_bottom = simple_draw.get_point(x1, y)
            right_top = simple_draw.get_point(x2, y + y1)
            simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=simple_draw.COLOR_CYAN, width=1)
            x1 += length
            x2 += length
    else:
        x1 = length / 2
        x2 = length * 1.5
        for _ in range(7):
            left_bottom = simple_draw.get_point(x1, y)
            right_top = simple_draw.get_point(x2, y + y1)
            simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=simple_draw.COLOR_CYAN, width=1)
            x1 += length
            x2 += length
    y += width

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()
