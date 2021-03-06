# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

FE = "function_errors.log"


def log_errors(func):
    def fun_error(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exp:
            log_string = f'{func.__name__} {type(exp)} {args if args else ""}{kwargs if kwargs else ""} {exp}'
            with open(FE, mode='a', encoding='utf-8') as function_errors:
                function_errors.write(f'{log_string}\n')
            raise exp  # можно даже просто raise - выбросится именно пойманное исключение
            # try:  А функцию func вызвали уже раннее, второй раз её выполнять смысла нет
            #     raise func(*args, **kwargs)  Выбросить исключение надо именнно "дальше", а не ловить его тут.
            #                           Надо чтобы код вызвавший декорированную функцию сам мог обработать исключение
            # except ZeroDivisionError as exp:
            #     print(f'Invalid format: {exp}')

    return fun_error


# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

# зачет!
