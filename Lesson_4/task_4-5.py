# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# Eugeniy's variant:

from functools import reduce
#
# def my_list(el_1, el_2):
#     return el_1 * el_2
#
# new_list = [el for el in range(100, 1001, 2)]
# print(f'Список\n{new_list}\nУмножение\n{reduce(my_list, new_list)}')

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))