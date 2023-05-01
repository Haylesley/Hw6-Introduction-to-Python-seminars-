# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент,разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент арифметической прогрессии: "))
b = int(input("Введите разность: "))
c = int(input("Введите количество элементов: "))

# def ArifmetProgr(a,b,c):
#     array = [a]
#     summ = a
#     for i in range(c-1):
#         summ = summ + b
#         array.append(summ)
#     print(array)

# ArifmetProgr(a,b,c)

summ = a

for i in range(c):
    print(summ, end = " ")
    summ = summ + b
