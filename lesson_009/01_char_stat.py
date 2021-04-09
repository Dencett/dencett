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
        self.stat_for_generate = None

    def get_data(self):
        with open(self.filename, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_for_line(line=line)

    def collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                self.stat[char] += 1

    def statistics_output(self):
        total = 0
        print('+---------+----------+\n'
              '|  буква  | частота  |\n' 
              '+---------+----------+')
        for char, quantity in self.stat_for_generate:
            total += quantity
            print(f'|{char:^9}|{quantity:^10}|')
        print(f'+---------+----------+\n'
              f'|{"итого":^9}|{total:^10}|\n'
              f'+---------+----------+')

    def get_sorted_stat(self):
        self.stat_for_generate = sorted(self.stat.items(), key=itemgetter(1), reverse=True)
        return self.stat_for_generate


zfile_name = 'python_snippets\\voyna-i-mir.txt'

statistics = Statistics(zfile_name)
statistics.get_data()
statistics.get_sorted_stat()
statistics.statistics_output()


class Statistics1(Statistics):

    def get_sorted_stat(self):
        self.stat_for_generate = sorted(self.stat.items(), key=itemgetter(1), reverse=False)
        return self.stat_for_generate


statistics_1 = Statistics1(zfile_name)
statistics_1.get_data()
statistics_1.get_sorted_stat()
statistics_1.statistics_output()


class Statistics2(Statistics):

    def get_sorted_stat(self):
        self.stat_for_generate = sorted(self.stat.items(), key=itemgetter(0), reverse=False)
        return self.stat_for_generate


statistics_2 = Statistics2(zfile_name)
statistics_2.get_data()
statistics_2.get_sorted_stat()
statistics_2.statistics_output()


class Statistics3(Statistics):

    def get_sorted_stat(self):
        self.stat_for_generate = sorted(self.stat.items(), key=itemgetter(0), reverse=True)
        return self.stat_for_generate


statistics_3 = Statistics3(zfile_name)
statistics_3.get_data()
statistics_3.get_sorted_stat()
statistics_3.statistics_output()


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

# TODO: не обязательно к выполнению. Но желательно.
#  Прочитайте, ознакомьтесь, можете задать вопросы, если что-то смущает.
#  TOD0 ниже нацелены на улучшение стиля, а именно на повышение читабельности кода (да, уже неплох, но можно улучшить),
#       и на оптимизацию затрат по памяти.
#  .
#  1. get_data - можно переименовать. Данный метод ничего не возвращает. Он скорее собирает или парсит данные.
#                По возможности надо давать имена, значение которых отражает суть того, что делает метод.
#                Данный метод не является "геттером", но начинается с "get_*", что несколько путаем.
#  2. get_sorted_stat - можно убрать сохранение в поле "self.stat_for_generate" и сделать сразу "return sorted(...)"
#               Сам же метод начать вызывать ВНУТРИ statistics_output, в цикле:
#                   for char, quantity in self.get_sorted_stat()
#  3. убрать поле "self.stat_for_generate", т.к. мы храним данные в 2х экземплярах:
#               self.stat и self.stat_for_generate, а это тратит память.

# зачет!