'''1. Найти сумму и произведение цифр трехзначного числа,
    которое вводит пользователь.'''

number = input('Введите число: ')

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)
print(f"Сумма цифр числа {number}: {sum}")
print(f"Произведение цифр: {number}: {prod}")
