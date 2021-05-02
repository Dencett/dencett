# -*- coding: utf-8 -*-

import os
import time
import shutil
import zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class Icons:

    def __init__(self, path, new_path):
        self.path = path
        self.new_path = new_path

    def determine_the_file(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                self.determine_the_time(full_file_path, file)

    def determine_the_time(self, full_file_path, file):
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        self.create_folders(file_time)
        self.copy_icons(full_file_path, file_time, file)

    def create_folders(self, file_time):
        os.makedirs(os.path.join(self.new_path, str(file_time[0]), str(file_time[1])),
                    exist_ok=True)

    def copy_icons(self, full_file_path, file_time, file):
        shutil.copy2(full_file_path,
                     os.path.join(self.new_path, str(file_time[0]), str(file_time[1]),
                                  str(file)))


path = 'icons'
new_path = 'icons_by_years'
path_zip = 'icons.zip'

# icons = Icons(path, new_path)
# icons.determine_the_file()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html

# print(path)
# zip_file = zipfile.ZipFile('icons.zip')
# for file in zip_file.namelist():
#     filename = os.path.basename(file)
#     if filename:
#         date = zip_file.getinfo(file).date_time
#         os.makedirs(os.path.join(new_path, str(date[0]), str(date[1])),
#                     exist_ok=True)
#         final_path = os.path.join(new_path, str(date[0]), str(date[1]), filename)
#         member = zip_file.open(file)
#         target = open(final_path, mode="wb")
#         shutil.copyfileobj(member, target)


class IconsZip:

    def __init__(self, path_zip, new_path):
        self.path_zip = path_zip
        self.new_path = new_path

    def determine_the_file(self):
        zip_file = zipfile.ZipFile(self.path_zip)
        for file in zip_file.namelist():
            filename = os.path.basename(file)
            if filename:
                self.determine_the_time(file, filename, zip_file)

    def determine_the_time(self, file, filename, zip_file):
        date = zip_file.getinfo(file).date_time
        self.create_folders(date)
        self.copy_icons(file, filename, date, zip_file)

    def create_folders(self, date):
        os.makedirs(os.path.join(self.new_path, str(date[0]), str(date[1])),
                    exist_ok=True)

    def copy_icons(self, file, filename, date, zip_file):
        final_path = os.path.join(self.new_path, str(date[0]), str(date[1]), filename)
        member = zip_file.open(file)
        target = open(final_path, mode="wb")
        shutil.copyfileobj(member, target)


icons_zip = IconsZip(path_zip, new_path)
icons_zip.determine_the_file()