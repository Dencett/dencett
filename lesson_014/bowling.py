from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def get_points(self):
        pass


class Nothing(State):

    def get_points(self):
        pass


class Strike(State):

    def get_points(self):
        return 20


class Spare(State):

    def get_points(self):
        return 15


class Bowling:

    def __init__(self, game_result):
        self.game_result = game_result
        self.state = Nothing()
        self.total_score = 0
        self.frame_number = 0
        self.first_element = True
        self.symbol = None

    def change_state(self, state):
        self.state = state

    def count_points(self, element):
        if element == '-':
            return 0
        else:
            return int(element)

    def get_strike(self):
        self.state = Strike()
        self.total_score += self.state.get_points()
        self.frame_number += 1

    def get_spare(self):
        self.state = Spare()
        self.total_score += self.state.get_points()
        self.first_element = True
        self.frame_number += 1

    def get_points(self, element):
        if element == '0':
            raise ValueError('Неверный ввод!')
        else:
            if self.first_element is True:
                self.symbol = element
                self.first_element = False
            else:
                self.total_score += self.count_points(self.symbol)
                self.total_score += self.count_points(element)
                self.first_element = True
                self.frame_number += 1

    def gets_score(self):
        for element in self.game_result:
            if element == 'X':
                self.get_strike()
            elif element == '/' and self.first_element is False:
                self.get_spare()
            elif element.isdigit() or element == '-':
                self.get_points(element)
            elif self.first_element is False:
                raise ValueError('Неверный ввод!')
            else:
                raise ValueError('Неверный ввод!')
        if self.first_element is False:
            raise ValueError('Неверный ввод!')
        elif self.frame_number > 10:
            raise ValueError('Сделано больше попыток!')
        elif self.frame_number < 10:
            raise ValueError('Сделано меньше попыток!')
        else:
            return self.total_score
# TODO Для реализации на паттерне "Состояние" нужно сделать классы: "ПервыйБросок", "ВторойБросок" (это два стейта -
#  состояния) .
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
