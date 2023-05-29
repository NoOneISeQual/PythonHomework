# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

from random import randint
monet = int(input('Введите кол-во монеток: '))
monet_0 = 0
monet_1 = 0
total_monet = 0
for i in range(monet):
    monet_count = randint(0,1)
    print(monet_count)
    if monet_count == 0:
        monet_0 += 1
    else:
        monet_1 += 1
    if monet_0 < monet_1:
        total_monet = monet_0
    else:
        total_monet = monet_1
print(f'минимально кол-во монет, которые нужно перевернуть составляет: {total_monet}')
