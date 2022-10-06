# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов

list = [2.3, 4, 3.5, 4.06]
min = list[0]
max = 0
for i in range(len(list)):
    
    if max < list[i]:
        max = list[i]
    if min > list[i]:
        min = list[i]
dif = (max - int(max)) - (min - int(min))

print(list)
print(max, min)
print(round(dif,2))



exit()
def dif (lst):
    for e in lst:
        print (e%1.2)
    return e


list = [2.3, 4, 3.5, 4.06]
print (dif(list))

