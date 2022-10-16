# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

from lib2to3.pgen2.literals import simple_escapes


def multipliers (n):
    new_list = []
    for i in range(2, int(n / 2) + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if n % i == 0:
                n = n / i
                new_list.append(i)
    return new_list

num = int(input('Введите число: '))
print (multipliers(num))
