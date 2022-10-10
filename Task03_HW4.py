# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

num = int(input('Введите число: '))
list = []
for i in range(1, num+1):
    list.append(random.randint(-num, num+1))
print(list)
list_new = []
for i in list:
    if list.count(i) == 1:
        list_new.append(i)
print(list_new)