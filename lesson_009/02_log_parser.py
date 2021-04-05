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


from collections import Counter


class Events:

    def __init__(self, filename):
        self.filename = filename
        self.val_list = []

    def get_data(self, adjustment):
        with open(self.filename, mode='r') as file:
            for line in file:
                val1, val2, key = line.split()
                if 'NOK' in line:
                    val = val1[1:] + ' ' + val2[:5]
                    adjustment_val = '[' + val[:adjustment] + ']'
                    self.val_list.append(adjustment_val)

    def dictionary_output(self, file_name):
        val_vocabulary = Counter(self.val_list)
        with open(file_name, 'w', encoding='utf-8') as file:
            for key, quantity in val_vocabulary.items():
                file.write(f'{key} {quantity}\n')


filename = 'events.txt'
events = Events(filename)
events.get_data(None)
events.dictionary_output('result-file.txt')

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
