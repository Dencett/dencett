#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

# NOTE импортировать модули всегда нужно выше всех остальных строк кода, пустых строк и комментариев (кроме двух первых)

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
london_moscow = ((london[0] - moscow[0]) ** 2 + (london[1] - moscow[1]) ** 2) ** .5  # TODO вместо этого можно просто
# TODO использовать переменную moscow_london. Дистанция же получается та же! Зачем тогда дублировать действия?

distances['London'] = {}
distances['London']['Paris'] = london_paris
distances['London']['Moscow'] = london_moscow

distances['Paris'] = {}
distances['Paris']['London'] = london_paris
distances['Paris']['Moscow'] = moscow_paris

pprint(distances)

# TODO в целом у Вас очень хороший вариант решения! Попробуйте улучшить код: создайте словарь distances "одним махом".
#  Вы создали 3 пустых словаря внутри distances, а затем начали по 1ому добавлять в него ключи. Сделайте так:
#       1. так же используйте готовые переменные (moscow_paris, london_paris, moscow_london);
#       2. создайте словарь distances "одним махом". Т.е. при создании мы заодно инициализируем словарь.
#          Пример инициализации словаря при создании:
#           color_yellow = 'желтый'
#           color_red = 'Красная'
#           fairytale_heroes = {
#              'Колобок': {
#                  'Колобок': color_yellow,
#                  'Дед': 'старый',
#                  'Бабка': 'молодая',
#              },
#              'Красная Шапочка': {
#                  'Шапочка': color_red
#              }
#          }
#      .
#      В примере мы создаем словарь fairytale_heroes, который имеет 2 Вложенных словаря: по ключу 'Колобок' и
#      по ключу 'Красная Шапочка'. Аналогично можно проинициализировать и distances:
#        distances = {
#           ...
#        }
#      Это сделает код компактнее и удобнее для понимания. Одного взгляда будет достаточно, чтобы понять, что хранится
#      в словаре и какую структуру он имеет. Особенно удобно, когда словарь имеет большой размер или используется в
#      качестве конфигурации чего-либо.
#      .
#     В итоге для получения расстояния, например, между Москвой и Парижем, можно использовать оба выражения:
#          distances['Moscow']['Paris']
#          distances['Paris']['Moscow']        # оба доступны
