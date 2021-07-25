# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

TICKET = os.path.join('images', 'ticket_template.png')
FONT_PATH = 'ofont.ru_Roboto.ttf'
FILLED_TICKET = 'ticker.png'


# def make_ticket(fio, from_, to, date):
#     image = Image.open(TICKET)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype(FONT_PATH, size=14)
#     data_dict = {fio: (50, 125), from_: (50, 194), to: (50, 260), date: (285, 260)}  # отлично!
#     for data, location in data_dict.items():
#         draw.text(location, data.upper(), font=font, fill=ImageColor.colormap['black'])
#     image.save(FILLED_TICKET)
#
#
# if __name__ == '__main__':
#     fio = input('Ф.И.О.: ')
#     from_ = input('Откуда: ')
#     to = input('Куда: ')
#     date = input('Дата: ')
#     make_ticket(fio, from_, to, date)

# зачет!

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

# def make_ticket(fio, from_, to, date, save_to):
#     image = Image.open(TICKET)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype(FONT_PATH, size=14)
#     data_dict = {fio: (50, 125), from_: (50, 194), to: (50, 260), date: (285, 260)}  # отлично!
#     for data, location in data_dict.items():
#         draw.text(location, data.upper(), font=font, fill=ImageColor.colormap['black'])
#     image.save(save_to)

def createParser():  # TODO имя функции пишут только маленькими буквами с подчёркиванием между словами
    parser = argparse.ArgumentParser()
    parser.add_argument('fio')
    parser.add_argument('from_')
    parser.add_argument('to')
    parser.add_argument('date')
    parser.add_argument('-s', '--save_to', default=FILLED_TICKET)
    return parser


if __name__ == '__main__':
    parser = createParser()
    ticket_parser = parser.parse_args()
    print(ticket_parser.fio, ticket_parser.from_, ticket_parser.to, ticket_parser.date, ticket_parser.save_to)
