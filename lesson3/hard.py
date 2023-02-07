
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

date = ''

while date != 0:
    date = input('Введите дату в формате dd.mm.yyyy (для выхода введите 0): ')
    if len(date) == 10:
        dd, mm, yyyy = date.split('.')
        if len(dd) == 2 and len(mm) ==2 and len(yyyy) == 4:
            if (int(dd) >= 1 and int(dd) <= 30) and (int(mm) >= 1 and int(mm) <= 12) and (int(yyyy) >= 1 and int(
                    yyyy) <=
                                                                                         9999 ):
                print(f'Вы ввели корректную дату: {date}, спасибо!')
                break
            else:
                print('Дата некорректна, попробуйте снова.')
        else:
            print('Дата некорректна, попробуйте снова.')
    elif len(date) < 10:
        print('Дата некорректна, попробуйте снова')
    elif len(date) > 10:
        print('Дата некорректна, попробуйте снова')


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2

num_room = int(input('Введите номер комнаты: '))

tower = []
floors_counter = 0
rooms_counter = 0
doors_counter = 0
stages_counter = 0

while rooms_counter < num_room:
    stages_counter += 1

    for stage in range(stages_counter):
        floors_counter += 1
        floor = []

        for doors_counter in range(stages_counter):
            rooms_counter += 1
            floor.append(rooms_counter)
            if rooms_counter == num_room:
                print(f'Ваш номер комнаты: {num_room}\nЭтаж: {floors_counter}\nДверь слева: {doors_counter + 1}')
