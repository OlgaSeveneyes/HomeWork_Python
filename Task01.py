# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [23, 5, 10, 1, 15, 3, 127]
sum = 0
for i in range (1, len(list), 2):
    sum += list[i]
print (sum)

# вариант 2

def sum (lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    return sum

list = [23, 5, 10, 1, 15, 3, 127]
print (sum(list))

