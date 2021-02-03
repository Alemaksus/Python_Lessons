# Игра угадай число:

# Шаг 1. Загадать случайное число +
import random

number = random.randint(1, 100)
print(number) # для реальной игры это нужно закомментить, чтобы не видеть загаданное число

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности из 3-х возможных: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)

print(users)

is_wwinner = False
winner_name = None

while not is_wwinner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        # Шаг 2. Предложить пользователю ввести число
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_wwinner = True
            winner_name = user
            break
        # Шаг 3. Сравнение чисел. Вывод результата
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'Победитель {winner_name}')