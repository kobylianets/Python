time = int(input("Введите время в секундах: "))
min = time // 60
hours= min // 60
sec = time % 60
print('Время {}:{}:{}'.format(hours, min, sec))