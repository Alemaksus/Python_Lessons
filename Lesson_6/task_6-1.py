# Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый,зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TrafficLight:
    __color = 'red'

    def running(self):
        print('TrafficLight has been switched on')

        self.__color = 'red'
        print(f'Traffic light is: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Attention: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f"Let's go: {self.__color}")
        time.sleep(7)

        while True:
            self.running()

working_tl_1 = TrafficLight()
print(working_tl_1.running())