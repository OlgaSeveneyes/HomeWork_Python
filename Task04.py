# Напишите программу, которая будет преобразовывать десятичное число в двоичное

num = int(input('Введите число для преобразования: '))
print(bin(num).replace("0b",""))

# вариант 2

def transform (n):
    a = ''
    while n > 0:
        a += str(n % 2)  
        n = n // 2
    return a

num = int(input('Введите число: '))
print (transform(num))