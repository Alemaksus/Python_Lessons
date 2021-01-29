# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# print(len(open('task_2.txt', 'r').readlines()))
# print(len(set(open('task_2.txt', 'r').read().split())))

# Eugene variants:

# Вариант 1:

with open('2.txt', 'r', encoding='utf-8') as f:
    usefulness - [f'{line}. {' '.join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    print(*usefulnes, f'всего строк - {len(usefulness)} ', sep='\n')

# Вариант 2:

lines_n = 0
words_n = 0
f = open('2.txt, 'r)
for line in f:
    lines_n += 1 # - подсчет длины линий
    words = line.split()
    words_n += len(words) # - подсчет кол-ва слов в строке
f.close()
print(lines_n)
print(words_n)
