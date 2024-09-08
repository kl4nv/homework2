import os
import time


for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join('C', 'Users', 'Кирилл', 'PycharmProjects', 'lesson2', 'module 7.5', 'module 7.5.py')
        filetime = os.path.getmtime('module 7.5.py')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize('module 7.5.py')
        parentdir = os.path.dirname(r'C\Users\Кирилл\PycharmProjects\lesson2\module 7.5\module 7.5.py')
    print(
        f'Обнаружен файл: {'module 7.5.py'}, '
        f'Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
        f'Родительская директория: {parentdir}')