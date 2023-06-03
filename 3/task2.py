# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# 5
# 1 2 3 4 5

# 6
# -> 5

from random import randint

list_length = int(input('Введите длину списка: '))
number = int(input('Введите число: '))
my_list = []
total_number = 0

for i in range(list_length):
    my_list.append(randint(1,10))
    for k in range(i):
        if my_list[i] == number:
            total_number = my_list[i]
        
print(list_length)
print(my_list)
print(number)
print(total_number)

#Abs модуль числа делает из отрицальных числе положительные 