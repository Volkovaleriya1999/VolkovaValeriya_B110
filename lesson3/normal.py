# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

from math import sqrt

list_num = [1, 6, 58, -4, 25, -36, 81]
new_num_list = []

for num in list_num:
    num1 = num ** 0.5
    if  num >= 0 and num1.is_integer():
        new_num_list.append(sqrt(num))

print(new_num_list)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input('Введите дату вашего рождения в формате dd.mm.yyyy: ').split('.')
days = {
    '01': 'первого', '02': 'второго', '03': 'третьего', '04': 'четвертого',
    '05': 'пятого', '06': 'шестого', '07': 'седьмого', '08': 'восьмого',
    '09': 'девятого', '10': 'десятого', '11': 'одинадцатого',
    '12': 'двенадцатого', '13': 'тринадцатого','14': 'четырнадцатого',
    '15': 'пятьнадцатого', '16': 'шестьнадцатого', '17': 'семнадцатого',
    '18': 'восемнадцатого', '19': 'девятнадцатого', '20': 'двадцатого',
    '21': 'двадцать первого', '22': 'двадцать второго',
    '23': 'двадцать третьего', '24': 'двадцать четвертого',
    '25': 'двадцать пятого', '26': 'двадцать шестого',
    '27': 'двадцать седьмого', '28': 'двадцать восьмого',
    '29': 'двадцать девятого', '30':'дридцатого', '31': 'тридцать первого'
}
month = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
    '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
    '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
}

print(f'Твой день рождения {days[date[0]]} {month[date[1]]} {date[2]} года')


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

from random import randint

n = int(input('Введите длину списка: '))
random_nums = []
count = 0
while count <= n:
    num = randint(-100, 100)
    random_nums.append(num)
    count += 1

print(random_nums)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 5, 3, 8, 2, 8, 4, 2, 1, 9, 6]

recurring_nums = list({x for x in lst if lst.count(x) > 1})
print(recurring_nums)

for i in recurring_nums:
    for j in lst:
        if i == j:
            lst.remove(j)
print(lst)


