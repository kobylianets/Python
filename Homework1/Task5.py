revenue = int(input("Введите значение выручки вашей фирмы:"))
costs = int(input("Введите значение издержек вашей фирмы:"))
if revenue > costs:
    print("Ваша фирма работает в прибыль")
elif revenue == costs:
    print("Ваша фирма работает в ноль")
else:
    print("Ваша фирма работает в убыток")