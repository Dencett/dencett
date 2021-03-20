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

# TODO здесь ваш код


from operator import itemgetter

# zfile_name = 'C:\\Users\\Владимир\\PycharmProjects\\python_base\\lesson_009\\python_snippets\\voyna-i-mir.txt'
#
# stat = {}
#
# with open(zfile_name, 'r', encoding='cp1251') as file:
#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 if char in stat:
#                     stat[char] += 1
#                 else:
#                     stat[char] = 1
#
# stat_for_generate = sorted(stat.items(), key=itemgetter(1), reverse=True)
# total = 0
# print('''+---------+----------+
# |  буква  | частота  |
# +---------+----------+''')
# for char in stat_for_generate:
#     total += char[1]
#     print(f'|{char[0]:^9}|{char[1]:^10}|')
#
#
# print(f'''+---------+----------+
# |{'итого':^9}|{total:^10}|
# +---------+----------+''')


class Statistics:

    def __init__(self, filename):
        self.filename = filename
        self.stat = {}

    def get_data(self):
        with open(self.filename, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_for_line(line=line)

    def collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    print(self.stat)
                else:
                    self.stat[char] = 1

    def generate(self):
        stat_for_generate = sorted(self.stat.items(), key=itemgetter(1), reverse=True)
        total = 0
        print('''+---------+----------+
        |  буква  | частота  |
        +---------+----------+''')
        for char in stat_for_generate:
            total += char[1]
            print(f'|{char[0]:^9}|{char[1]:^10}|')
        print(f'''+---------+----------+
        |{'итого':^9}|{total:^10}|
        +---------+----------+''')


zfile_name = 'C:\\Users\\Владимир\\PycharmProjects\\python_base\\lesson_009\\python_snippets\\voyna-i-mir.txt'
statistics = Statistics(zfile_name)
statistics.generate()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
