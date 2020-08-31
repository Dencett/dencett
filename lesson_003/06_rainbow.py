# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
i = 0
x = 50
a = 350
for _ in range(7):  # TODO цвет можно получить сразу в цикле, если задать его по списку rainbow_colors, а не range()
    start_point = sd.get_point(x, 50)
    end_point = sd.get_point(a, 450)
    color = rainbow_colors[i]
    x += 5
    a += 5
    i += 1
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)


# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(400, -180)
radius = 500
i = 7
while i > 0:  # TODO гораздо проще задать цикл for сразу по списку цветов
    i -= 1  # TODO а как задать обратный порядок цветов см. в предыдущей теме решение задания 07_secret.py ;)
    color = rainbow_colors[i]
    for _ in range(7):
        radius += 4
        sd.circle(center_position=point, radius=radius, color=color, width=4)


sd.pause()
