# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла.

fruits1 = ['apple', 'banana', 'orange', 'kiwi', 'pear']

fruits2 = ['banana', 'kiwi', 'tangerine']

result = []

for fruit in fruits1:
    if fruit in fruits2:
        result.append(fruit)

print(result)

# Можно записать короче через генератор:

result = [fruit for fruit in fruits1 if fruit in fruits2]

print(result)