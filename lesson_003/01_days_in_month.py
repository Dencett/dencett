# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input('Введите, пожалуйста, номер месяца: ')
month = int(user_input)  # TODO что произойдёт, если пользователь введёт что-либо кроме числа?
# TODO попробуйте реализовать проверку используя .isdigit() или .isnumeric()
print('Вы ввели', month)

if month == 1:
    print('В этом месяце 31 день!')
elif month == 2:
    print('В этом месяце 28 дней!')
elif month == 3:
    print('В этом месяце 31 день!')
elif month == 4:
    print('В этом месяце 30 дней!')
elif month == 5:
    print('В этом месяце 31 день!')
elif month == 6:
    print('В этом месяце 30 дней!')
elif month == 7:
    print('В этом месяце 31 день!')
elif month == 8:
    print('В этом месяце 31 день!')
elif month == 9:
    print('В этом месяце 30 дней!')
elif month == 10:
    print('В этом месяце 31 день!')
elif month == 11:
    print('В этом месяце 30 дней!')
elif month == 12:
    print('В этом месяце 31 день!')
else:
    print('Hомер месяца некорректен!')

# TODO решение правильное, но эти две строки кода крайне неэффективны с точки зрения как чтения, так и поддержки
#  сохраните данные номеров месяцев в списки и проверяйте вхождение month в нужный список
#  (можно задать их прямо в условной конструкции, по одному списку для случая с 31 днём и 30 и отдельно обработать с 28)
