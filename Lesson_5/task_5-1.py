# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

task_1 = open("out_file.txt", "w")
str_list = ['input(Введите ваше имя: )\n', 'input(Введите ваш возраст: )\n', '         ']
task_1.writelines(str_list)
task_1.close()


