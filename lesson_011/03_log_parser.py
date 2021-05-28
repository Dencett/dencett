# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


from collections import defaultdict


class Events:

    def __init__(self, filename):
        self.filename = filename
        self.val_vocabulary = []
        self.event_count = 0

    def __iter__(self):
        self.val_vocabulary = []
        self.event_count = 1
        return self

    def __next__(self):
        with open(self.filename, mode='r', encoding='cp1251') as file:
            for line in file:
                val1, val2, key = line.split()
                if 'NOK' in line:
                    val = val1[1:] + ' ' + val2[:5]
                    if val not in self.val_vocabulary:
                        if self.val_vocabulary == []:
                            self.val_vocabulary.append(val)
                        else:
                            self.val_vocabulary.append(val)
                            return self.val_vocabulary[-2], self.event_count
                        self.event_count = 1
                    else:
                        self.event_count += 1
            else:
                raise StopIteration()

    def parse_line(self, val):
        return val[:]


filename = 'events.txt'

# events = Events(filename)
# grouped_events = Events(filename)
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')


def events(filename):
    val_vocabulary = defaultdict(int)
    with open(filename, mode='r') as file:
        for line in file:
            val1, val2, key = line.split()
            if 'NOK' in line:
                val = val1[1:] + ' ' + val2[:5]
                val_vocabulary[val] += 1
        for group_time, event_count in val_vocabulary.items():
            yield group_time, event_count


grouped_events = events(filename)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

