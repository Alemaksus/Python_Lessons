# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py
# всех функций. Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.

import randomlist

from folders import create_folders, delete_folders

create_folders()
delete_folders()
print(randomlist.get_random([1, 2, 3]))
print(randomlist.get_random([1]))