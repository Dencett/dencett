from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def throw(self, element):
        pass


class FirstThrow(State):

    def throw(self, element):
        if element == 'X':
            return 20
        if element == '-':
            return 0
        elif element.isdigit():
            return int(element)


class SecondThrow(State):

    def throw(self, element):
        if element == '/':
            return 15
        if element == '-':
            return 0
        elif element.isdigit():
            return int(element)


class Bowling:

    def __init__(self, game_result):
        self.game_result = game_result
        self.state = FirstThrow()
        self.total_score = 0
        self.frame_number = 0
        self.first_throw = True
        self.symbol = None

    def change_state(self, state):
        self.state = state

    def gets_score(self):
        for element in self.game_result:
            if self.first_throw is True:
                if element == 'X':
                    self.total_score += self.state.throw(element)
                    self.frame_number += 1
                elif element == '-' or element.isdigit():
                    self.symbol = self.state.throw(element)
                    self.state = SecondThrow()
                    self.first_throw = False
                else:
                    raise ValueError('Неверный ввод!')
            else:
                if element == '/' or element == '-' or element.isdigit():
                    if element == '-' or element.isdigit():
                        if self.state.throw(element) + self.symbol >= 10:
                            raise ValueError('Неверный ввод!')
                        else:
                            self.total_score += self.state.throw(element) + self.symbol
                    else:
                        self.total_score += self.state.throw(element)
                    self.frame_number += 1
                    self.state = FirstThrow()
                    self.first_throw = True
                else:
                    raise ValueError('Неверный ввод!')
        if self.first_throw is False:
            raise ValueError('Неверный ввод!')
        elif self.frame_number > 10:
            raise ValueError('Сделано больше попыток!')
        elif self.frame_number < 10:
            raise ValueError('Сделано меньше попыток!')
        else:
            return self.total_score
#
# Стейт должен брать как параметр следующий символ из входной строки и возвращать скоринг и следующий стейт.
# Общий алгоритм:
#
# текущий_стейт, скор = ПервыйБросок(), 0
# цикл для каждого символа из строки результата:
#     текущий_стейт, очков = текущий_стейт.рассчитать(символ)
#     скор += очков
#
# скор - общее количество очков, то есть результат
#
# Можно ещё добавить класс Менеджера и поместить в него код инициализации первого броска и тела цикла.
