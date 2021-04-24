# -*- coding: utf-8 -*-

import os
import time
import shutil

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


# TODO: сейчас класс разбирает по папкам даже слишком хорошо. Он должен складывать картинки приблизительно так:
#  результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#  .
#  А он помимо месяца добавляет еще и день:
#       icons_by_year/2018/05/24/cat.jpg
#       icons_by_year/2018/05/25/man.jpg
#       icons_by_year/2017/12/31/new_year_01.jpg
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


# TODO: а если мы захотим взять из папки icons и из папки icons2?
#  А положит в папку icons_by_years и icons_by_years_new?
path = 'icons'
new_path = 'icons_by_years'
icons = Icons(path, new_path)
icons.determine_the_file()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# TODO: Пример разархивации файла.
#  Давайте сначала проверять информацию о файле, а потом сразу извлекать его туда, где ему положено лежать.
#  .
#  Пример:
#      file = zip_file.namelist()[100500]               # берем файл из архива
#      filename = os.path.basename(file)                # получаем имя файла (без абсолютного пути)
#      if filename:
#         date = zip_file.getinfo(file).date_time       # получена дата последней модификации. Теперь можно
#      final_path = f'...'                              # создать путь ... только join! никаких f-строк!)
#      member = zip_file.open(file)
#      target = open(..., mode="wb")                    # "wb" - запись бинарных данных (не текст, а бинарный код)
#      shutil.copyfileobj(member, target)               # копируем из архива