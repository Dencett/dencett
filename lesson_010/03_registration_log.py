# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

FF = 'registrations.txt'
BAD = 'registration_bad.log'
GOOD = 'registraton_good.log'


class NotNameError(Exception):

    def __str__(self):
        return ' Содержит цифры'


class NotEmailError(Exception):

    def __str__(self):
        return ' Некорректно указан E-mail'


def check(line):
    data = line.split()
    if len(data) < 3:
        raise ValueError(' Недостаточно данных')
    name, mail, year = line.split(' ')
    symbols = ('@', '.')
    if year.isdigit() is True:
        age = int(year)
    else:
        raise ValueError(' Данные не в том порядке')
    if name.isalpha() is False:
        raise NotNameError
    elif age not in range(10, 99):
        raise ValueError(' По возрасту не подходит')
    else:
        for char in symbols:
            if char not in mail:
                raise NotEmailError
    return line


with open(FF, mode='r', encoding='utf-8') as ff, \
    open(BAD, mode='a', encoding='utf-8') as bad, \
        open(GOOD, mode='a', encoding='utf-8') as good:
    for line in ff:
        line = line[:-1]
        try:
            string = check(line)
        except (NotNameError, NotEmailError, ValueError) as exc:
            bad.write(f'{line} {exc} \n')
        else:
            good.write(f'{line} \n')

# зачет!
