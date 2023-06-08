# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

A_number = int(input("Введите первое неотрицительное число "))
B_number = int(input("Введите второе неотрицательно число "))


def sum(A_number, B_number):
    if A_number == 0:
        return B_number
    else:
        return sum(A_number - 1, B_number + 1)


print(sum(A_number, B_number))