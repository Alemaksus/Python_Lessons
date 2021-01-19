earnings = int(input('Введите сумму выручки за 2020 год в тысячах рублей: '))
cost = int(input('Введите сумму издержек за 2020 год в тысячах рублей: '))
income = earnings - cost
losses = cost - earnings
if income > 0:
    print('Ваша компания получила прибыль за 2020 год. Поздравляем!!!')
else:
    print('Вы получили убыток за 2020 год. Не отчаивайтесь, следующий год будет наверняка успешнее')
if income > cost:
    profitability = income / earnings
number_of_employees = int(input('Введите количество сотрудников вашей компании: '))
profitability = (income / earnings) * 1000
profit_per_employee = profitability / number_of_employees
print('Прибыль в расчете на одного сотрудника составила в 2020 году: ', ("%.2f" % ((profitability/profit_per_employee))))