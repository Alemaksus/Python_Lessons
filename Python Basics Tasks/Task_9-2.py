# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

# My variant:

# def My_funk():
#     numbers = input('Введите три числа ')
#     return max(numbers)
#
# print(My_funk())

# Teacher's variant:

def get_max(a, b, c):
    result = max([a, b, c])
    return result

result = get_max(1, 5, 3)
print(result)
