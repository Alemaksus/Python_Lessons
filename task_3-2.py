#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# My variant:

# def create_customer():
#
#     user = {'name': '', 'surname': '', 'year_birth': '', 'city': '', 'email': '', 'phone': ''}
#     for key, value in user.items():
#         value = input(f'Введите {key} - ')
#         user[key] = value
#     return user
#
# def start():
#     user = create_customer()
#     print(f"{user}")
#
# start()

# Почему то не форматируется user в строку через f-строку.

# Eugene variant:

def personal_inf(**kwargs):
    return ' '.join(kwargs.values())

name = input('Введите name - ')
surname = input('Введите surname - ')
birthday = input('Введите birthday - ')
city = input('Введите city - ')
email = input('Введите email - ')
phone = input('Введите phone - ')

print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))
