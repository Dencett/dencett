# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
from multiprocessing import Process, Pipe

volatility_dict = {}
zero_volatility = []


class Trader(Process):
    def __init__(self, path, conn):
        super(Trader, self).__init__()
        self.path = path
        self.conn = conn

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
            self.conn.send([secid, volatility])


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
    tickers, pipes = [], []
    parent_conn, child_conn = Pipe()
    for file in get_path_list(path):
        ticker = Trader(file, child_conn)
        tickers.append(ticker)
        pipes.append(parent_conn)
    for ticker in tickers:
        ticker.start()
    for conn in pipes:
        secid, volatility = conn.recv()
        if volatility > 0:
            volatility_dict[secid] = volatility
        else:
            zero_volatility.append(secid)
    for ticker in tickers:
        ticker.join()
    measure_volatility()


if __name__ == '__main__':
    tickers_files('trades')
