# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

list = [10, 8, 8, 7, 7, 7, 6, 5, 5, 4, 3, 3, 3, 2,2, 1]
number = int(input('Введите новый элемент рейгинга: '))
i = 0

for n in list:
    if number <= n:
        i += 1

list.insert(i, float(number))
print(list)