# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

print ('Введите число: ')
num = int(input())
mult = 1
for i in range(num):
    i += 1
    mult *= i
    print (mult)