# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер новой клетки после сложения равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка стала меньше и теперь она равна: {sub}' if sub > 0 else 'Ничего не получилось'

    def __truediv__(self, other):
        return f'Результатом деления двух клеток стало: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Две клетки преумножились и получилась одна большая клетка: {self.quantity * other.quantity}'

cell = Cell(8)
cell_2 = Cell(12)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)