num_1 = int(input('Введите целое положительное число: '))
i = -1
while num_1 > 10:
    x = num_1 % 10
    num_1 //= 10
    if x > i:
        i = x
print(i)


