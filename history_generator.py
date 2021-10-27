def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(f'history: {history}')
            continue
        result = x + y
        print(f'result: {result}')
        history.append(result)


c = calc()
type(c)  # <type 'generator'>

next(c)  # Необходимая инициация. Можно написать c.send(None)

c.send([1, 2])
c.send([3, 5])
c.send([661, 666])
c.send(['h', 0])

c.close()  # Закрываем генератор