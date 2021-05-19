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

class NotNameError(Exception):

    def __str__(self):
        return ' Содержит цифры'


class NotEmailError(Exception):

    def __str__(self):
        return ' Некорректно указан E-mail'


def check(line):
    data = line.split()
    if len(data) < 3:
        ValueError(' Неверные данные')  # TODO укажите точнее проблему (и далее везде)
    name, mail, year = line.split(' ')
    symbols = ('@', '.')
    if year.isdigit() is True:
        age = int(year)
    else:
        raise ValueError(' Неверные данные')
    if name.isalpha() is False:
        raise NotNameError
    elif age not in range(10, 99):
        raise ValueError(' Неверные данные')
    else:
        for char in symbols:
            if char not in mail:
                raise NotEmailError
    return line


with open('registrations.txt', mode='r', encoding='utf-8') as ff, \
    open('registration_bad.log', mode='a', encoding='utf-8') as bad, \
        open('registraton_good.log', mode='a', encoding='utf-8') as good:
    # TODO Имена файлов надо присваивать константам и использовать в основном коде только их.
    #  Имена констант пишутся большими буквами. Располагают константы в начале модуля, сразу после
    #  импортов сторонних модулей.
    #  Может возникнуть необходимость изменить имя файла и через константу это делать удобнее - константа это
    #  единое место изменения, а примениться она может во многих местах. Поэтому вверху её легко найти для изменения
    #  без необходимости перелопачивания кода проекта.

    for line in ff:
        line = line[:-1]
        try:
            string = check(line)
        except (NotNameError, NotEmailError, ValueError) as exc:
            bad.write(line + f'{exc}' + '\n')  # TODO f-строки позволяют избежать конкатенации, исправьте, пожалуйста
        else:
            good.write(line + '\n')

# зачет!
