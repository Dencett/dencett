from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def throw(self, element, game_place):
        pass


class FirstThrow(State):

    def throw(self, element, game_place):
        if element == 'X':
            if game_place == 'local':
                return 20
            elif game_place == 'global':
                return 10
        elif element == '0':
            raise ValueError('Неверный ввод!')
        elif element == '-':
            return 0
        elif element.isdigit():
            return int(element)
        elif element == '/':
            raise ValueError('Неверный ввод!')


class SecondThrow(State):

    def throw(self, element, game_place):
        if element == '/':
            if game_place == 'local':
                return 15
            elif game_place == 'global':
                return 10
        elif element == '0':
            raise ValueError('Неверный ввод!')
        elif element == '-':
            return 0
        elif element.isdigit():
            return int(element)
        elif element == 'X':
            raise ValueError('Неверный ввод!')


class Game:

    def __init__(self, game_result):
        self.game_result = game_result
        self.state = FirstThrow()
        self.total_score = 0
        self.frame_number = 0
        self.first_throw = True
        self.symbol = None

    def change_state(self, state):
        self.state = state

    def get_first_throw(self, element):
        pass

    def get_second_throw(self, element):
        pass

    def gets_score(self):
        for element in self.game_result:
            if self.first_throw is True:
                self.get_first_throw(element)
            else:
                self.get_second_throw(element)
        if self.first_throw is False:
            raise ValueError('Неверный ввод!')
        elif self.frame_number > 10:
            raise ValueError('Сделано больше попыток!')
        elif self.frame_number < 10:
            raise ValueError('Сделано меньше попыток!')
        else:
            return self.total_score


# class Bowling(Game):
#
#     def __init__(self, game_result):
#         super().__init__(game_result)
#         self.game_place = 'local'
#
#     def get_first_throw(self, element):
#         if element == 'X':
#             self.total_score += self.state.throw(element, self.game_place)
#             self.frame_number += 1
#         elif element == '-' or element.isdigit():
#             self.symbol = self.state.throw(element, self.game_place)
#             self.state = SecondThrow()
#             self.first_throw = False
#         else:
#             raise ValueError('Неверный ввод!')
#
#     def get_second_throw(self, element):
#         if element == '/' or element == '-' or element.isdigit():
#             if element == '-' or element.isdigit():
#                 if self.state.throw(element, self.game_place) + self.symbol >= 10:
#                     raise ValueError('Неверный ввод!')
#                 else:
#                     self.total_score += self.state.throw(element, self.game_place) + self.symbol
#             else:
#                 self.total_score += self.state.throw(element, self.game_place)
#             self.frame_number += 1
#             self.state = FirstThrow()
#             self.first_throw = True
#         else:
#             raise ValueError('Неверный ввод!')

class Bowling(Game):

    def __init__(self, game_result):
        super().__init__(game_result)
        self.index = -1
        self.game_place = 'global'

    def get_first_throw(self, element):
        self.index += 1
        if element == 'X':
            self.total_score += self.state.throw(element, self.game_place)
            self.frame_number += 1
            if self.index >= 1:
                if self.game_result[self.index - 1] == 'X':
                    self.total_score += self.state.throw(element, self.game_place)
        elif element == '-' or element.isdigit():
            self.symbol = self.state.throw(element, self.game_place)

            self.state = SecondThrow()
            self.first_throw = False
        else:
            raise ValueError('Неверный ввод!')
        if self.index >= 2:
            if self.game_result[self.index - 2] == 'X':
                self.total_score += self.state.throw(element, self.game_place)
            if self.game_result[self.index - 1] == '/':
                self.total_score += self.state.throw(element, self.game_place)

    def get_second_throw(self, element):
        self.index += 1
        if element == '/' or element == '-' or element.isdigit():
            if element == '-' or element.isdigit():
                if self.state.throw(element, self.game_place) + self.symbol >= 10:
                    raise ValueError('Неверный ввод!')
                else:
                    self.total_score += self.state.throw(element, self.game_place) + self.symbol
            else:
                self.total_score += self.state.throw(element, self.game_place)
            if self.index >= 2:
                if self.game_result[self.index - 2] == 'X':
                    if element == '-' or element.isdigit():
                        self.total_score += self.state.throw(element, self.game_place) + self.symbol
                    else:
                        self.total_score += self.state.throw(element, self.game_place)
            self.frame_number += 1
            self.state = FirstThrow()
            self.first_throw = True
        else:
            raise ValueError('Неверный ввод!')


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
