'''5. Пользователь вводит две буквы. Определить, на каких местах алфавита они
стоят и сколько между ними находится букв.'''

letter1, letter2 = [
  x.upper() for x in input('Введите две буквы, через пробел (A - Z): ').split()
]

# Генерация списка букв
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

index_letter1 = abc_list.index(letter1) + 1
index_letter2 = abc_list.index(letter2) + 1

if index_letter1 < index_letter2:
    step = 1
else:
    step = -1

print(f'Первая буква {letter1}, находится на позиции: {index_letter1}')
print(f'Вторая буква {letter2}, находится на позиции: {index_letter2}')

print(
    f'Между ними находятся буквы \
{abc_list[abc_list.index(letter1) + step:abc_list.index(letter2):step]} \
({abs(index_letter1 - index_letter2) - 1})'
        )
