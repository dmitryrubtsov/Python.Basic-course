'''5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве.'''

import random

r = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)

if r[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {r[min_index]}.',
            f'Находится в массиве на позиции {min_index}')
