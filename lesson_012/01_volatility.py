# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


import os
from operator import itemgetter

volatility_dict = {}
zero_volatility = []


class Trader:
    def __init__(self, path):
        self.path = path

    def run(self):
        with open(self.path) as file:
            line = next(file)
            secid, tradetime, price, quantity = line.split(',')
            price_min = price
            price_max = price
            price_header = price
            while True:
                line = next(file, 'end')
                if line == 'end':
                    break
                secid, tradetime, price, quantity = line.split(',')
                if price_min == price_header and price_max == price_header:
                    price_min = float(price)
                    price_max = float(price)
                if price_min > float(price):
                    price_min = float(price)
                if price_max < float(price):
                    price_max = float(price)
            half_sum = (price_max + price_min) / 2
            volatility = round(((price_max - price_min) / half_sum) * 100, 2)
            if volatility > 0:
                volatility_dict[secid] = volatility
            else:
                zero_volatility.append(secid)


def get_path_list(path):
    file_list = []
    for name, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(name, file)
            file_list.append(path)
    return file_list


def measure_volatility():
    order_of_volatility = sorted(volatility_dict.items(), key=itemgetter(1), reverse=True)
    print('Максимальная волатильность:')
    for ticker, volatility in order_of_volatility[:3]:
        print(f'{ticker} {volatility} %')
    print('Минимальная волатильность:')
    for ticker, volatility in order_of_volatility[-1:-4:-1]:
        print(f'{ticker} {volatility} %')
    print('Нулевая волатильность:')
    print(', '.join(zero_volatility))


def tickers_files(path):
    for file in get_path_list(path):
        trader = Trader(file)
        trader.run()
    measure_volatility()


if __name__ == '__main__':
    tickers_files('trades')
