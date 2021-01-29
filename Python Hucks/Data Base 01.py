# Template of simple a data base:

users = []

while True:
    print('1. Ввести данные\n2. Вывести данные\n3. Выход')
    i = input('Выберите пункт меню - ')

    if i == '1':
        data = input('Выведите имя и возраст через пробел - ').split()
        users.append({'name': data[0], 'age': data[1]})

    elif i == '2':
        print(users)

    elif i == '3':
        break

    else:
        print('Повторите ввод!')