# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4


a_number = int(input('Введите первое число: '))
b_number = int(input('Введите второе число: '))

def rec_sum(a_number,b_number):
    if a_number == 0:
        return b_number
    return rec_sum(a_number -1,b_number +1)

print(rec_sum(a_number,b_number))