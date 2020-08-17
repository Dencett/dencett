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

# distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5
#
# distances['Moscow'] = {}
# distances['Moscow']['London'] = moscow_london
# distances['Moscow']['Paris'] = moscow_paris
#
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
# london_moscow = moscow_london
#
# distances['London'] = {}
# distances['London']['Paris'] = london_paris
# distances['London']['Moscow'] = london_moscow
#
# distances['Paris'] = {}
# distances['Paris']['London'] = london_paris
# distances['Paris']['Moscow'] = moscow_paris

distances = {
    'Moscow': {
        'London': moscow_london,
        'Paris': moscow_paris
    },
    'London': {
        'Moscow': moscow_london,
        'Paris': london_paris
    },
    'Paris': {
        'London': london_paris,
        'Moscow': moscow_paris
    }
}

pprint(distances)

# зачёт! 🚀
