# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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


import os
from operator import itemgetter
from threading import Thread

volatility_dict = {}
zero_volatility = []


class Trader(Thread):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.need_stop = False

    def run(self):
        with open(self.path) as file:
            next(file)
            line = next(file)
            secid, tradetime, price, quantity = line.split(',')
            price_min = float(price)
            price_max = float(price)
            for line in file:
                secid, tradetime, price, quantity = line.split(',')
                price = float(price)
                if price_min > price:
                    price_min = price
                if price_max < price:
                    price_max = price
            half_sum = (price_max + price_min) / 2
            volatility = round(((price_max - price_min) / half_sum) * 100, 2)
            if volatility > 0:
                # TODO плохо что класс работает с переменными из глобальной области неявно - передавайте их объекту при
                #  его создании (т.е. через параметры метода __init__)
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
    # TODO Если сделать вывод минимальных волатильностей согласно заданию (цитата: Волатильности указывать в порядке
    #  убывания.), то срез будет проще
    print('Нулевая волатильность:')
    print(', '.join(zero_volatility))


def trader_run(tickers):
    for ticker in tickers:
        ticker.start()
    for ticker in tickers:
        ticker.join()


def tickers_files(path):
    tickers = [Trader(file) for file in get_path_list(path)]
    trader_run(tickers)
    measure_volatility()


if __name__ == '__main__':
    tickers_files('trades')
