# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func_1(num1 = int(input('Введите первое число: ')), num2 = int(input('Введите второе число не равное 0: '))):
    return num1 / num2
print(my_func_1())

# не понял как внутри позиционной функции проверить на ошибку с нулем :-(
