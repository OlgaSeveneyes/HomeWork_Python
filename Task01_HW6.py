# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

num = int(input('Введите число: '))
list1 = [random.randint(-num, num+1) for i in range(1, num+1)]
print(list1)

list_new = [i for i in list1 if list1.count(i) == 1]
print(list_new)

# вариант 2

list_new2 = list(filter(lambda i: list1.count(i) == 1, list1))
print(list_new2)