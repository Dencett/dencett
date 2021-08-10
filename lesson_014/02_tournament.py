# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>

import argparse
from bowling import Bowling
from collections import defaultdict
from operator import itemgetter


class Tournament:

    def __init__(self, open_file, new_file):
        self.open_file = open_file
        self.new_file = new_file
        self.winners = defaultdict(int)
        self.gamers = defaultdict(int)
        self.points_dict = {}

    def show_points(self):
        for line in self.open_file:
            if line != '\n':
                self.new_file.write(f'{self.count_points(line)} \n')
            else:
                self.new_file.write('\n')

    def count_points(self, line):
        data = line.split()
        if len(line.split()) == 3 and data[1] == 'Tour':
            return f'{data[0]} {data[1]} {data[2]}'
        elif len(line.split()) == 2:
            data = line.split()
            name, result = data
            bowling = Bowling(result)
            try:
                points = bowling.gets_score()
            except Exception as exc:
                self.gamers[name] += 1
                return f'{name} {result} {exc}'
            else:
                self.points_dict[name] = points
                self.gamers[name] += 1
                return f'{name} {result} {points}'
        elif len(line.split()) == 3 and data[0] == 'winner':
            if self.points_dict != {}:
                winner = max(self.points_dict, key=self.points_dict.get)
                self.winners[winner] += 1
                self.points_dict.clear()
                return f'{data[0]} {data[1]} {winner}'
            else:
                return f'{data[0]} {data[1]} None'

    def show_result(self):
        gamers = sorted(self.gamers.items(), key=itemgetter(1), reverse=True)
        print('+----------+------------------+--------------+\n'
              '| Игрок    |  сыграно матчей  |  всего побед |\n'
              '+----------+------------------+--------------+')
        for gamer, quantity in gamers:
            if gamer not in self.winners:
                self.winners[gamer] = 0
            print(f'|{gamer:^10}|{quantity:^18}|{self.winners[gamer]:^14}|')
        print('+----------+------------------+--------------+')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    tournament_parser = parser.parse_args()
    with open(tournament_parser.input, mode='r', encoding='utf-8') as open_file, \
            open(tournament_parser.output, mode='a', encoding='utf-8')as new_file:
        tournament = Tournament(open_file, new_file)
        tournament.show_points()
        tournament.show_result()

# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+
