# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class Division_by_zero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def division(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"На ноль делить нельзя")


div = Division_by_zero(50, 2)
print(Division_by_zero.division(15, 0))
print(Division_by_zero.division(10, 3))