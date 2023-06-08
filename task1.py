# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

A_number = int(input('Введите первое число(А): '))
B_number = int(input('Введите второе число(В): '))

def func(A_number, B_number):
    if B_number == 0:
        return 1 
    return A_number ** B_number

print(func(A_number, B_number))