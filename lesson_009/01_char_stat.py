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

    def generate_output(self, stat_for_generate):
        total = 0

        # TODO: посмотрите на print после цикла. Этот print надо так же причесать
        print('''+---------+----------+ 
|  буква  | частота  | 
+---------+----------+''')
        for char, quantity in stat_for_generate:
            total += quantity
            print(f'|{char:^9}|{quantity:^10}|')

        # TODO: вот это нормальный print. Почему? Потому что ''' используют как правило для текста, очень большого.
        #  У нас вывод ниже +\- показывает как будет выглядеть напечатнный текст.
        #  Для print`а выше будет еще лучше смотреться.
        print(f'+---------+----------+'
              f'|{"итого":^9}|{total:^10}|'
              f'+---------+----------+''')


    def get_sorted_stat(self, stat_for_generate):
        """
        Метод сортирует переданную в него статистику. Но почему-то ничего не возвращает, хотя называется get_sorted_stat
        А как правило get_* означает "вернуть какие-то данные".

        :param stat_for_generate:

        """
        # TODO: получается, что get_sorted_stat вместе возврата статистики вызывает generate_output.
        #  Да еще и делает это от имени какой-то переменной statistics
        statistics.generate_output(stat_for_generate)


zfile_name = 'python_snippets\\voyna-i-mir.txt'

# TODO: программист, использовавший класс не знал, что нужно создавать объект только по имени statistics, и назвал
#  его так, как сам посчитал нужным. Класс начал падать
statistics_100500 = Statistics(zfile_name)
statistics_100500.get_data()

# TODO: строка ниже - вот что должен возвращать метод get_sorted_stat.
#  И пусть он вызывается внутри generate_output
stat_for_generate = sorted(statistics_100500.stat.items(), key=itemgetter(1), reverse=True)
statistics_100500.get_sorted_stat(stat_for_generate)

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
