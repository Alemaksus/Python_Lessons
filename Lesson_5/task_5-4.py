# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = ['Один','Два', 'Три', 'Четыре']
changed = []

with open("task_4-in.txt", "r") as f_obj:
    content = f_obj.readlines()
    print(content)

e = len(content)
j = 0

for i in content:
    b = i
    c = i.find(' ')
    d = i[:c]
    r = b.replace(d, rus[j])
    j = j + 1
    changed.append(r)
    with open ('task_4-out.txt', "w") as f_new:
        f_new.writelines(changed)
        print(f_new)
