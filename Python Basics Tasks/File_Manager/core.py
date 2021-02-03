# Файловый Менеджер

import os  # - это нужно для создания и работы с папками и расширения функционала менеджера
import shutil
import datetime

# 1. Функцмя для создания файла

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

# 2. Функция для создания папки

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')

# 3. Расширение функционала: получение списка файлов через генератор пути директории

def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]  # - фильтр через генератор списка
    print(result)

# 4. Удаление файла

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)

# 5. Копирование файлов и папок:

def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)

# 6. Запись информации о работе менеджера в файл

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8' ) as f:
        f.write(result + '\n')

def change_dir(name):
    os.chdir(name)
    print(os.getcwd())

# Проверка работы функций:

if __name__ == '__main__':  # - 'это не позволит выполняться данной проверке при импорте данной функции в др файл
    create_file('text.dat')
    create_file('text dat', 'some text')
    create_folder('new_f')  # - запустить 2 раза, чтобы выловить ошибку FileExistError и обработать его
    get_list()
    get_list(True)
    delete_file('new_f')
    delete_file('text.dat')
    copy_file('new_f', 'new2')
    create_file('text.dat')
    copy_file('text.dat', 'text2.dat')
    save_info('abc')
