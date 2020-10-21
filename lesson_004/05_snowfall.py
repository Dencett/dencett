# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 500)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snow_x_list = []
snow_y_list = []
length_list = []

for _ in range(N):
    snow_x_list.append(sd.random_number(80, 800))
    snow_y_list.append(sd.random_number(500, 700))
    length_list.append(sd.random_number(20, 100))

while True:
    sd.clear_screen()
    for i, x in enumerate(snow_x_list):
        y = snow_y_list[i]
        length = length_list[i]
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
        snow_y_list[i] -= 10
        if snow_y_list[i] < 50:
            break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# зачёт первой части

# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать


while True:
    sd.start_drawing()
    for i, x in enumerate(snow_x_list):
        length = length_list[i]
        point = sd.get_point(snow_x_list[i], snow_y_list[i])
        sd.snowflake(center=point, length=length, color=sd.background_color)
        if snow_y_list[i] > 50:
            snow_y_list[i] -= 10
            point_fall = sd.get_point(snow_x_list[i], snow_y_list[i])
            sd.snowflake(point_fall, length=length, color=sd.COLOR_WHITE)
        else:
            last_point = sd.get_point(snow_x_list[i], snow_y_list[i])
            sd.snowflake(last_point, length, color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


while True:
    sd.start_drawing()
    for i, x in enumerate(snow_x_list):
        length = length_list[i]
        point = sd.get_point(snow_x_list[i], snow_y_list[i])
        sd.snowflake(center=point, length=length, color=sd.background_color)
        if snow_y_list[i] > 50:
            snow_y_list[i] -= 10
            snow_x_list[i] -= sd.random_number(-10, 10)
            point_fall = sd.get_point(snow_x_list[i], snow_y_list[i])
            sd.snowflake(point_fall, length=length, color=sd.COLOR_WHITE)
        else:
            last_point = sd.get_point(snow_x_list[i], snow_y_list[i])
            sd.snowflake(last_point, length, color=sd.COLOR_WHITE)
            snow_y_list[i] += sd.random_number(600, 800)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()

# зачёт! 🚀
