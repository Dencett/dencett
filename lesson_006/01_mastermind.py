# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT


from mastermind_engine import guess_number, check_number, fun_bulls_and_cows, end_game

guess_number()
player_turn = 1
print('Ход: ', player_turn)
while True:
    input_user = input('Загадайте четырехзначное число: ')
    if input_user.isdigit():
        user_number = [int(i) for i in input_user]
        if len(user_number) != 4:
            print('Ввод некорректен, введите четыре числа')
        elif user_number[0] == 0:
            print('Ввод некорректен, первое число не должен быть 0')
        elif len(user_number) != len(set(user_number)):
            print('Ввод некорректен, все числа должны быть разными')
        else:
            if check_number(user_number):
                print('Вы выиграли')
                print('Количество ходов: ', player_turn)
                print('Хотите еще партию?')
                print('Да - 1')
                print('Нет - 2')
                input_selection = input('Введите: ')
                if input_selection.isdigit():
                    player_selection = int(input_selection)
                    if player_selection == 1:
                        end_game()
                        player_turn = 1
                        continue
                    elif player_selection == 2:
                        break
                    else:
                        print('Ввод некорректен')
                else:
                    print('Ввод некорректен')
                    # TODO здесь переход происходит на новое загаданное число, а не повторную попытку ввода 1 или 2.
            else:
                fun_bulls_and_cows(user_number)
                player_turn += 1
                print('Ход: ', player_turn)
    else:
        print('Ввод некорректен, введите числа')
