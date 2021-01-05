#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def create_customer():

    user = {'name': '', 'surname': '', 'year_birth': '', 'city': '', 'email': '', 'phone': ''}
    for key, value in user.items():
        value = input(f'Введите {key} - ')
        user[key] = value
    return user

def start():
    user = create_customer()
    print(f"{user}")

start()

# Почему то не форматируется user в строку через f-строку.