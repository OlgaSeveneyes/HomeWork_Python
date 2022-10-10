# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов

def dif (lst):
    new_list = []
    for i in lst:
        if i % 1 != 0:
            new_list.append(round(i%1, 3))
    return (max(new_list) - min(new_list))

list = [0.05, 5, 4.32, 1, 6.987, 3]
print (dif(list))

