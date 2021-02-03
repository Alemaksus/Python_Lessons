# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
# и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# plan = {}
# with open('task_5-6.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         subject, lecture, practice, lab = line.split()
#         plan[subject] = int(lecture) + int(practice) + int(lab)
#     print(f'Расписание: \n {plan}')

# Должно бы работать, но пишет: "ValueError: too many values to unpack (expected 4)".
# Не знаю что предпринять.

# Eugene's variant:

mydict = {}
with open('6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':') # побеждаем двоеточие и сразу получаем имя
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '3' and i <= '9')]).split())) # - это генератор
        # + фильтр на числа и получаем кол-во часов, т.е. по сути это простой парсер (!!!)
        mydict[name] = name_sum
print(f'{mydict}')