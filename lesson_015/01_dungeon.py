# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...


from decimal import Decimal
import json
import re
import csv
import datetime

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']
csv_data = []


def process_a_string(line):
    if type(line) is dict:
        for key in line.keys():
            # print(re.search(r'[0-9A-Za-z]+', k)[0])
            tm_line = (re.search(r'tm\d+', key)[0])
            tm = (re.search(r'\d+', tm_line)[0])
            return tm
    else:
        # print(re.search(r'[0-9A-Za-z]+', ks)[0])
        exp_line = (re.search(r'exp\d+', line)[0])
        exp = (re.search(r'\d+', exp_line)[0])
        tm_line = (re.search(r'tm\d+', line)[0])
        tm = re.search(r'\d+', tm_line)[0]
        return exp, tm


def add_information_to_csv_file(current_location, current_experience):
    current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    csv_data.append({field_names[0]: current_location,
                     field_names[1]: current_experience,
                     field_names[2]: current_date
                     })


class Dungeon:

    def __init__(self, locations, remaining_time):
        self.locations = locations
        self.choice = 0
        self.choice_dict = {}
        self.locations_list = []
        self.location_name = None
        self.experience = Decimal('0')
        self.revival = False
        self.game_over = 'game_over'
        self.gameplay = True
        self.remaining_time = Decimal(remaining_time)
        self.elapsed_time = 0

    def get_started(self):
        for location in self.locations.keys():
            self.location_name = location
        for key in self.locations.keys():
            self.locations_list = self.locations[key]
        print(self.location_name)
        self.revival = False
        self.remaining_time = Decimal(remaining_time)
        self.experience = Decimal('0')

    def explore_location(self):
        print(f'Вы находитесь в {self.location_name}')
        print(f'У вас {self.experience} опыта и осталось {self.remaining_time} секунд до наводнения')
        print(f'Прошло уже {datetime.timedelta(seconds=self.elapsed_time)}\n')
        if self.remaining_time <= 0:
            print('-----------------------------------\n'
                  'Вы не успели открыть люк!!! НАВОДНЕНИЕ!!!')
            self.resurrect()

    def consider_actions(self):
        print('Внутри вы видите:')
        for loc in self.locations_list:
            if type(loc) is dict:
                self.choice_dict[str(self.choice)] = loc
                for loc_name in loc.keys():
                    print(f'- Вход в локацию {loc_name} ')
            else:
                self.choice_dict[str(self.choice)] = loc
                print(f'- Монстра {loc}')
        print('\nВыберите действие:')
        for loc in self.locations_list:
            self.choice += 1
            if type(loc) is dict:
                self.choice_dict[str(self.choice)] = loc
                for key in loc:
                    print(f'{self.choice}. Перейти в локацию {key} ')
            else:
                self.choice_dict[str(self.choice)] = loc
                print(f'{self.choice}. Убить монстра {loc}')
        self.choice += 1
        self.choice_dict[str(self.choice)] = self.game_over
        print(f'{self.choice}. Сдаться и выйти из игры')
        self.choice = 0

    def choose_action(self, solution):
        if solution not in self.choice_dict.keys():
            print('Выберите заново')
        else:
            for choice_key in self.choice_dict.keys():
                if solution == choice_key:
                    if type(self.choice_dict[choice_key]) is dict:
                        for key in self.choice_dict[choice_key].keys():
                            self.location_name = key
                            tm = process_a_string(self.choice_dict[choice_key])
                            self.remaining_time -= Decimal(tm)
                            self.elapsed_time += float(tm)
                            print('-----------------------------------')
                            print(f'Вы перешли в локацию {key}!')
                            self.locations_list = self.choice_dict[choice_key][key]
                            if self.locations_list == "You are winner":
                                if self.experience < 280:
                                    print('-----------------------------------\n'
                                          'Увы, Вам не хватает опыта для открытия люка')
                                    self.resurrect()
                                else:
                                    print('Ура, Вы выбрались')
                                    self.gameplay = False
                        add_information_to_csv_file(self.location_name, self.experience)
                    elif self.choice_dict[choice_key] == self.game_over:
                        self.gameplay = False
                    else:
                        print('-----------------------------------')
                        print('Вы убили монстра!')
                        exp, tm = process_a_string(self.choice_dict[choice_key])
                        self.experience += Decimal(exp)
                        self.remaining_time -= Decimal(tm)
                        self.elapsed_time += float(tm)
                        self.locations_list.remove(self.choice_dict[choice_key])

    def resurrect(self):
        print('Вы теряете сознания!\n'
              'Приходите в сознание и видите, что вы в начале пещеры!\n'
              'Ну, на этот-то раз у вас все получится!\n'
              'Вы осторожно входите в пещеру.\n'
              '-----------------------------------')
        self.revival = True


with open('rpg.json', 'r') as json_file:
    locations_dict = json.load(json_file)
    dungeon = Dungeon(locations_dict, remaining_time)
    while True:
        if dungeon.gameplay is False:
            break
        dungeon.get_started()
        while True:
            if dungeon.revival is True:
                break
            dungeon.explore_location()
            if dungeon.revival is True:
                break
            dungeon.consider_actions()
            solution = input('Ваш выбор: ')
            dungeon.choose_action(solution)
            if dungeon.gameplay is False:
                break


with open('dungeon.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(csv_data)

# Учитывая время и опыт, не забывайте о точности вычислений!
