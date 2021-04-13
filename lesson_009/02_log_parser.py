# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


from collections import defaultdict


class Events:

    def __init__(self, filename):
        self.filename = filename
        self.val_vocabulary = defaultdict(int)

    def collect_data(self):
        with open(self.filename, mode='r') as file:
            for line in file:
                self.collect_for_line(line=line,)

    def collect_for_line(self, line):
        val1, val2, key = line.split()
        if 'NOK' in line:
            # TODO: что в строках ниже лишнее?
            val = val1[1:] + ' ' + val2[:5]
            self.parse_line(val)
            self.val_vocabulary[self.parse_line(val)] += 1

    def parse_line(self, val):
        return '[' + val[:] + ']'

    def dictionary_output(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            for key, quantity in self.val_vocabulary.items():
                file.write(f'{key} {quantity}\n')


filename = 'events.txt'

events = Events(filename)
events.collect_data()
events.dictionary_output('result-file.txt')


# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году

class Events1(Events):

    def parse_line(self, val):
        return '[' + val[:-6] + ']'


events_1 = Events1(filename)
events_1.collect_data()
events_1.dictionary_output('result-file.txt')


class Events2(Events):

    def parse_line(self, val):
        return '[' + val[:-9] + ']'


events_2 = Events2(filename)
events_2.collect_data()
events_2.dictionary_output('result-file.txt')


class Events3(Events):

    def parse_line(self, val):
        return '[' + val[:-12] + ']'


events_3 = Events3(filename)
events_3.collect_data()
events_3.dictionary_output('result-file.txt')

# зачет!