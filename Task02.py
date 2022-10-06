# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult (lst):
    mult_list = []
    for i in range((len(lst)+1)//2):
        mult_list.append(lst[i]*lst[len(lst)-1-i])
    return(mult_list)

list = [23, 5, 3, 10, 1]
print (mult(list))



