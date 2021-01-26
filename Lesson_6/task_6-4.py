# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость: {self.speed}'

class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'\nВы превысили скорость. Ваша скорость: {self.speed}'
        else:
            return f'Скорость{self.name} - в пределах нормы'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость. Ваша скорость: {self.speed}'
        else:
            return f'Скорость {self.name} - в пределах нормы'

class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 100:
            return f'\nВы превысили скорость. Ваша скорость: {self.speed}'
        else:
            return f'Скорость {self.name} - в пределах нормы'

town = TownCar('Рено', 80, 'оливковый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Болид', 200, 'красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('Газель', 30, 'серая', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())
