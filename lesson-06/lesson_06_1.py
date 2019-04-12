'''1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС.'''

'''
x86_64 GNU/Linux
Python 3.7.3
'''

'''lesson-03_9'''
import sys
import random

matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(15)])


min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print(
        'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
        min_list[0]
            )

sum_size = 0
sum_size += sys.getsizeof(matrix)
sum_size += sys.getsizeof(min_list)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(string)
sum_size += sys.getsizeof(j)

print('Переменные занимают', sum_size)
