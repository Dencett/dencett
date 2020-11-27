import simple_draw as sd
from random import randint


snow_list = []


def create_snowflakes(quantity):
    global snow_list
    if len(snow_list) == 0:
        for _ in range(quantity):
            snow_list.append([randint(80, 800), randint(500, 700), randint(20, 60)])


def paint_snowflakes_with_color(color):
    for coordinate in snow_list:
        length = coordinate[2]
        point = sd.get_point(coordinate[0], coordinate[1])
        sd.snowflake(center=point, length=length, color=color)


def move_snowflakes():
    for coordinate in snow_list:
        coordinate[1] -= 10


def numbers_reached_down_screen():
    for coordinate in reversed(snow_list):
        return coordinate[1] <= -60  # так тоже можно


def delete_snowflakes():
    for coordinate in reversed(snow_list):
        if coordinate[1] <= -60:
            snow_list.remove(coordinate)

