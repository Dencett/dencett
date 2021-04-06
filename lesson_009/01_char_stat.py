# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

from operator import itemgetter
from collections import defaultdict


class Statistics:

    def __init__(self, filename):
        self.filename = filename
        self.stat = defaultdict(int)

    def get_data(self):
        with open(self.filename, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_for_line(line=line)

    def collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                self.stat[char] += 1

    def statistics_output(self, stat_for_generate):
        total = 0
        print('+---------+----------+\n'
              '|  буква  | частота  |\n' 
              '+---------+----------+')
        for char, quantity in stat_for_generate:
            total += quantity
            print(f'|{char:^9}|{quantity:^10}|')
        print(f'+---------+----------+\n'
              f'|{"итого":^9}|{total:^10}|\n'
              f'+---------+----------+')

    def get_sorted_stat(self):
        stat_for_generate = sorted(statistics.stat.items(), key=itemgetter(1), reverse=True)
        self.statistics_output(stat_for_generate)


zfile_name = 'python_snippets\\voyna-i-mir.txt'
statistics = Statistics(zfile_name)
statistics.get_data()
statistics.get_sorted_stat()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
