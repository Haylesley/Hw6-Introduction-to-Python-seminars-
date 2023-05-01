# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_1 = []
for i in range(random.randint(10,20)):
    list_1.append(random.randint(-10,10))
print(list_1)

min_number = int(input("Введите минимальное число: "))
max_number = int(input("Введите максимальное число: "))

for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end= " ")