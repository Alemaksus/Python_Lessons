#  Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
#  Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва».

# My variant:
def user():
    name = input('Введите пожалуйста ваше имя: ')
    age = input('Сколько вам лет? ')
    city = input('В каком городе вы проживаете? ')
    return(f'{name}, {age} год(а), проживает в городе {city}')

print(user())

# Teacher's variant:

# def persom_info(name, age, city):
#     result = f'{name}, {age} год(а) проживает в городе {city}'
#     return result

# print(persom_info('Василий', 21, 'Москва'))