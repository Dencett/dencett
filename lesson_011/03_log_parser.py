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

FILENAME = 'events.txt'


class Events:

    def __init__(self, filename):
        self.filename = filename
        self.val_vocabulary = []
        self.event_count = 0
        self.result = True

    def __iter__(self):
        self.val_vocabulary = []
        self.event_count = 1
        self.file = open(self.filename, mode='r', encoding='cp1251')
        self.result = True
        return self

    def __next__(self):
        for line in self.file:
            val1, val2, key = line.split()
            if 'NOK' in line:
                val = val1[1:] + ' ' + val2[:5]
                if val not in self.val_vocabulary:
                    if self.val_vocabulary != []:
                        self.val_vocabulary.append(val)
                        quantity = self.event_count
                        self.event_count = 1
                        return self.val_vocabulary[-2], quantity
                    self.val_vocabulary.append(val)
                    self.event_count = 1
                else:
                    self.event_count += 1
        while self.result:
            self.result = False
            return self.val_vocabulary[-1], self.event_count
        self.file.close()
        raise StopIteration()


events = Events(FILENAME)
grouped_events = Events(FILENAME)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')


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


# grouped_events = events(FILENAME)
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')

