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

list_length = int(input('Введите длину массива: '))
number = int(input('Введите число, которое хотети найти: '))
list = []
number_count = 0

for i in range(list_length):
    list_length = randint(1,10)
    list.append(list_length)
    if list_length == number:
        number_count += 1
    else:
        number_count += 0

print (list)
print(number_count)