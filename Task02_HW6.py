# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [23, 5, 10, 1, 15, 3, 127]
new_lst = [lst[i] for i in range (1, len(lst), 2)]
sum=0
for j in range(len(new_lst)):
    sum += new_lst[j]
print(sum)

# или

lst = [23, 5, 10, 1, 15, 3, 127]
new_lst = [lst[i] for i in range (1, len(lst), 2)]
print(f'{sum(new_lst)}')