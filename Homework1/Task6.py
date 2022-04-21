revenue = int(input("Введите значение выручки вашей фирмы:"))
costs = int(input("Введите значение издержек вашей фирмы:"))
if revenue > costs:
    print("Ваша фирма работает в прибыль")
    rent = revenue / costs
    print("Рентабельность составляет {}".format(rent))
    number_employee = int (input("Введите число сотрудников вашей фирмы:"))
    revenue_employee = revenue / number_employee
    print("Прибыль на одного сотрудника вашей фирмы составляет {}".format(revenue_employee))

elif revenue == costs:
    print("Ваша фирма работает в ноль")
else:
    print("Ваша фирма работает в убыток")