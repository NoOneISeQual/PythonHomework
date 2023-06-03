# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

list_length = int(input('Введите длину списка: '))

number = int(input('Введите число, которое хотети найти: '))
my_list = []
number_count = 0

for i in range(list_length):
    temp = randint(1,10)
    my_list.append(temp)
    if temp == number:
        number_count += 1
    else:
        number_count += 0

print(list_length)
print (my_list)
print(number)
print(f'Число встречается {number_count} раз')

# У  списков есть метод каунт my_list.count считает сколько раз встречается число