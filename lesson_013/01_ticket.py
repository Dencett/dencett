# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

TICKET = os.path.join('images', 'ticket_template.png')
FONT_PATH = 'ofont.ru_Roboto.ttf'
FILLED_TICKET = 'ticker.png'


def make_ticket(fio, from_, to, date):
    image = Image.open(TICKET)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, size=14)
    data_dict = {fio: (50, 125), from_: (50, 194), to: (50, 260), date: (285, 260)}  # отлично!
    for data, location in data_dict.items():
        draw.text(location, data.upper(), font=font, fill=ImageColor.colormap['black'])
    image.save(FILLED_TICKET)


if __name__ == '__main__':
    fio = input('Ф.И.О.: ')
    from_ = input('Откуда: ')
    to = input('Куда: ')
    date = input('Дата: ')
    make_ticket(fio, from_, to, date)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
