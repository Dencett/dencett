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

    def generate_output(self, stat_for_generate, total):
        print('''+---------+----------+ 
|  буква  | частота  | 
+---------+----------+''')
        for char, quantity in stat_for_generate:
            total += quantity
            print(f'|{char:^9}|{quantity:^10}|')
        print(f'''+---------+----------+
|{'итого':^9}|{total:^10}|
+---------+----------+''')


class Generation(Statistics):

    def __init__(self, filename):
        super().__init__(filename)

    def get_data(self):
        super().get_data()

    def generate_output(self, stat_for_generate, total):
        super().generate_output(stat_for_generate, total)

    def generate(self, stat_for_generate):
        total = 0
        generation.generate_output(stat_for_generate, total)


zfile_name = 'python_snippets\\voyna-i-mir.txt'
generation = Generation(zfile_name)
generation.get_data()
stat_for_generate = sorted(generation.stat.items(), key=itemgetter(1), reverse=True)
generation.generate(stat_for_generate)

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
