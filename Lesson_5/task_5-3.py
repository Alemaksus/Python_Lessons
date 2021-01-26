# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.
# Вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("task_3.txt", 'r', encoding='utf-8') as salary:
    employee = {}
    for line in salary:
        key, value = line.split()
        employee[key] = value
        if int(value) < 20000:
            print(f'{key}: зарплата менее 20000')
        average_salary = sum(int(value)) / sum(str)
        print(average_salary)
