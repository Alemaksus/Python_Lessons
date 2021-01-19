# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func_3(a, b, c):
    x = [a, b, c]
    x.remove(min(a, b, c))
    return sum(x)

def start_my_func_3():
    print(my_func(12, 13, 10))