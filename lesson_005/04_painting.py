# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


import simple_draw as sd

from painting import rainbow
from painting import wall
from painting import fractal
from painting import window
from painting import sun
from painting import snowfall
from painting import human


sd.resolution = (1400, 900)
COLOR_DARK_ORANGE = (127, 63, 0)

sd.rectangle(left_bottom=sd.get_point(0, 0), right_top=sd.get_point(1400, 50), color=COLOR_DARK_ORANGE, width=0)

rainbow.draw_rainbow()
wall.draw_wall()
window.draw_window()
wall.draw_roof()
fractal.draw_branches(start_point=sd.get_point(1150, 50), angle=90, length=100)
sun.draw_sun()
human.draw_human()
snowfall.draw_snowfall()


sd.pause()


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
