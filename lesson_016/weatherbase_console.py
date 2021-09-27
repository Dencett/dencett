import peewee

from database_updater import DatabaseUpdater
from image_maker import ImageMaker

print('''Выбор действие:
1. Сохранить данные о погоде в базе данных;
2. Вывести данные о погоде;
3. Создать открытки с погодой.''')


while True:
    choice = input('Выберите действие: ')
    if int(choice) in range(1, 4):
        break

dbu = DatabaseUpdater()

if __name__ == '__main__':
    try:
        if choice == '1':
            dbu.save_data()
        elif choice == '2':
            for dw in dbu.get_data():
                print(dw)
        elif choice == '3':
            imagemaker = ImageMaker(dbu.get_data())
            imagemaker.get_image()
    except peewee.ProgrammingError:
        print('Нету базы!!!')
