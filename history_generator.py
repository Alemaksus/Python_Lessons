def calc():
    history = []
    while True:
        x, y = (yield)  # Прием данных из внешнего метода send (или функции)
        if x == 'h':
            print(f'history: {history}')
            continue
        result = x + y
        print(f'result: {result}')
        history.append(result)


c = calc()
type(c)  # <type 'generator'>

next(c)  # Необходимая инициация. Можно написать c.send(None)

c.send([1, 2])  # именно через send подаются разные входные данные на генератор
c.send([3, 5])
c.send([661, 666])
c.send(['h', 0])  # ключ h для

c.close()  # Закрываем генератор