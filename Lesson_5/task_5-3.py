# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.
# Вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# with open("task_3.txt", 'r', encoding='utf-8') as salary:
#     employee = {}
#     for line in salary:
#         key, value = line.split()
#         employee[key] = value
#         if int(value) < 20000:
#             print(f'{key}: зарплата менее 20000')
#         average_salary = sum(int(value)) / sum(str)
#         print(average_salary)

# Eugene variant:

with open('3.txt', 'r', encoding='unf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')